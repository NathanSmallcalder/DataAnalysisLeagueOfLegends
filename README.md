### Introduction

The project focuses on the data collection and data analysis of the popular video game League of Legends. The project uses docker, python and MySQL. 
Users can collect data using the DataCollection.py file or using the pre-existing data in the table setup script.

Setup MySQL

```
sudo docker pull mysql/mysql-server:latest

docker run --name=LeagueStats --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest

docker exec -it LeagueStats mysql -h localhost -P 3306 --protocol=tcp -u root -proot_password

```
### Database ERD

### Setup

To insert tables copy and paste the SQL script TableSetup.txt into the mysql interface.

Create a new ```config,py ``` with the following lines;

```python

api_key = "INSERT RIOT API KEY"
sql_password = "INSERT DATABASE PASSWORD"
sql_user = "INSERT DATABAESE NAME"
host = "INSERT HOST"
```

### Data Collection

To gather data, a script was created to query a single summoner, gathering in-depth statistics in their last 15 matches. This script gathered important match details, including match results, kills, damage, deaths, assists, and loadout. Data was gathered from the Riot Games API and stored in a MySQL database, the data from the table setup scripts contains data used on a [Previous Machine Learning Project](https://github.com/NathanSmallcalder/Dissertation]).

After creating the config.py file, the DataCollection.py Script can be run, due to rate limits the script will take a while to gather data.
Once data is gathered on a summoner, the user can be change by altering lines 31 and 32 to change the region or summoner's name.

```python

Region = "EUW1"
summonerName = "#####"

```

### Data Cleaning

Riot Games API can sometimes contain inconsistent role data if the player is assigned a role of support and spends more time in another portion of the map, they may be given an inaccurate role for the match or assigned the bot role, which is incorrect. To fix this issue, if a player's champion has an ID that is a support, and below a certain amount of minions killed, they will be assigned the role of support when preparing the data; which will help differentiate the two roles on the bottom lane.

### Data Visulization




### Limitations

The pre-existing data is from League of Legends Patch 13.6.1.



