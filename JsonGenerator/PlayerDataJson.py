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

cursor.execute("SELECT * FROM SummonerUserTbl")

data = cursor.fetchall()
# ID
id = getSummonerIdFromDatabase(summonerName)
# Damage Taken
DmgTaken = avgDmgTakenSummonerAll(id)
AllDamageT = avgDmgTakenAll()
# DamageDealt
DmgDealt = avgDmgDealtSummonerAll(id)
AllDamageD = avgDmgDealtAll()
# Gold Earnt
GoldEarnt = avgGoldSummonerAll(id)
AllGold = avgGoldAll()
#Dragon Kills
dragons = avgDragonAll()
summDragons = avgDragonSummoner(id)
#Baron Kills
barons = avgBaronAll()
summBarons = avgBaronSummoner(id)

## Data Sorting
SORT_ORDER = {"Unranked": 0 ,"Iron": 1, "Bronze": 2, "Silver": 3,"Gold": 4, "Platinum": 5,"Diamond": 6, "Master": 7, "Grandmaster": 7,"Challenger": 8}
AllDamageT.sort(key=lambda val: SORT_ORDER[val[0]])
AllDamageD.sort(key=lambda val: SORT_ORDER[val[0]])
AllGold.sort(key=lambda val: SORT_ORDER[val[0]])
dragons.sort(key=lambda val: SORT_ORDER[val[0]])
barons.sort(key=lambda val: SORT_ORDER[val[0]])

#Dataset
DataList = []
for ranks in barons:
    Data = {}
    Data["Rank"] = ranks[0]
    Data['AvgBaronKills'] = ranks[1]
    DataList.append(Data)

for data in DataList:
    for damage in AllDamageD:
        data['DamageDealt'] = damage[1]

for data in DataList:
    for damage in AllDamageT:
        data['DamageTaken'] = damage[1]
        
for data in DataList:
    for gold in AllGold:
        data['AvgGold'] = gold[1]
        
for data in DataList:
    for d in dragons:
        data['DragonDamage'] = d[1]

for data in DataList:
    data["AvgBaronKills"] = str(data["AvgBaronKills"])
    data["DamageDealt"] = str(data["DamageDealt"])
    data["DamageTaken"] = str(data["DamageTaken"])
    data["DragonDamage"] = str(data["DragonDamage"])
    data["AvgGold"] = str(data["AvgGold"])

print(DataList)
with open('Averages.json', 'w') as f:
    json.dump(DataList, f)


##
Dict = {
    "Rank": summonerName,
    "DragonDamage": summDragons[0][0],
    "DamageTaken":DmgTaken[0][0],
    "DamageDealt":DmgDealt[0][0],
    "AvgGold":GoldEarnt[0][0],
    "AvgBaronKills":summBarons[0][0],
}

Dict["DragonDamage"] = (str(Dict["DragonDamage"]))
Dict["DamageTaken"] = str(Dict["DamageTaken"])
Dict["DamageDealt"] = str(Dict["DamageDealt"])
Dict["AvgGold"] = str(Dict["AvgGold"])
Dict["AvgBaronKills"] = str(Dict["AvgBaronKills"])

print(Dict)
DataList.append(Dict)
print(DataList)
with open('PlayerData.json', 'w') as f:
    json.dump(Dict, f)

