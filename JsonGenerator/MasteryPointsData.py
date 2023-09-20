import sys
sys.path.append('..')
from config import *
from RiotApiCalls import *
import mysql.connector
import plotly.express as px
import pandas as pd
import json
## Database Connection
config = {
    'user': 'root',
    'password': 'root_password',
    'host': 'localhost',
    'port': 3306,
    'database': 'LeagueStats',
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

### Object Preperation
masteryList = []

### Account Config
region = "euw1"
summonerName = "Lil Nachty"

### API Quries
Summ = getSummonerDetails(region,summonerName)

print(Summ)
Mastery = getMasteryStats(region,Summ['id'])
print(Mastery)

### Data Prep
for points in Mastery:
    mastery = {}
    mastery['MasteryScore'] = points['championPoints']
    mastery['Champ'] = points['championId']
    mastery['Image'] = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/" + str(points['championId']) + ".png"
    masteryList.append(mastery)

df = pd.DataFrame(masteryList)

# Create the bubble chart
fig = px.scatter(df, x='MasteryScore', y='Champ', size='MasteryScore',
                 hover_name='Champ')

for i, row in df.iterrows():
    image_url = row['Image']
    fig.add_layout_image(
     
        x=row['Champ'],
        y=row['Champ'],
        sizex=5,
        sizey=5,
    )

# Update the layout
fig.update_layout(images=[], showlegend=False)

# Show the chart
fig.show()


with open('data.json', 'w') as f:
    json.dump(masteryList, f)