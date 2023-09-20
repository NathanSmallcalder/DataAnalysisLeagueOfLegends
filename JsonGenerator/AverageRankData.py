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


#Stats Per Rank
DmgD = avgDmgDealtAll()
DmgT = avgDmgTakenAll()
minions = avgMinionsAll()
barons = avgBaronAll()
dragons = avgDragonAll()

#Organise lists
SORT_ORDER = {"Unranked": 0 ,"Iron": 1, "Bronze": 2, "Silver": 3,"Gold": 4, "Platinum": 5,"Diamond": 6, "Master": 7, "Grandmaster": 7,"Challenger": 8}
DmgD.sort(key=lambda val: SORT_ORDER[val[0]])
DmgT.sort(key=lambda val: SORT_ORDER[val[0]])
minions.sort(key=lambda val: SORT_ORDER[val[0]])
barons.sort(key=lambda val: SORT_ORDER[val[0]])
dragons.sort(key=lambda val: SORT_ORDER[val[0]])

Stats = []

i = 0
for d in DmgD:
    Data = {}
    Data['Rank'] = d[0]
    Data['AverageDamageDealt'] = d[1]
    Data['AverageDamageTaken'] = DmgT[i][1]
    Data['AverageMinions'] = minions[i][1]
    Data['AverageBarons'] = barons[i][1]
    Data['AverageDragons'] = dragons[i][1]
    i = i + 1
    Stats.append(Data)

#CleanUp
for d in Stats:
    d['Rank'] = str(d["Rank"])
    d['AverageDamageDealt'] = str(d["AverageDamageDealt"])
    d['AverageDamageTaken'] = str(d["AverageDamageTaken"])
    d['AverageMinions'] = str(d["AverageMinions"])
    d['AverageBarons'] = str(d["AverageBarons"])
    d['AverageDragons'] = str(d["AverageDragons"])

with open('RankAverages.json', 'w') as f:
    json.dump(Stats, f)

