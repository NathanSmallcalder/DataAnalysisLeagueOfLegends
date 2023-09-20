import sys
sys.path.append('.')
from config import *
from RiotApiCalls import *
import mysql.connector
import pandas as pd
import json
from databaseQuries import *
import matplotlib.pyplot as plt
import numpy as np

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
summonerName = "Lil Nachty "

totalGames = getAllGamesCount()
print(totalGames)
champs = getChampionAverages()
DataList = []

for champ in champs:
    Data = {}
    Data["Champ"] = champ[0]
    Data['Kills'] = champ[1]
    Data["Deaths"] = champ[2]
    Data['Assists'] = champ[3]
    Data['Wins'] = champ[4]
    Data['GameDuration'] = champ[5]
    DataList.append(Data)
#Data Clean up
for data in DataList:
    data["Champ"] = str(data["Champ"])
    data["Kills"] = str(data["Kills"])
    data["Deaths"] = str(data["Deaths"])
    data["Assists"] = str(data["Assists"])
    data["Wins"] = str(data["Wins"])
    data["GameDuration"] = str(data["GameDuration"])

with open('ChampionStats.json', 'w') as f:
    json.dump(DataList, f)
