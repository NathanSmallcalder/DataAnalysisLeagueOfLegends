
### Introduction

The project focuses on the data collection and data analysis of popular video game League of Legends. The project uses docker, python and MySQL.

Setup MySQL

```
sudo docker pull mysql/mysql-server:latest

docker run --name=LeagueStats --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest

docker exec -it LeagueStats mysql -h localhost -P 3306 --protocol=tcp -u root -proot_password

```

To insert tables copy and paste the SQL script TableSetup.txt

Create a new ```config,py ``` with the following lines;

```python

api_key = "INSERT RIOT API KEY"
sql_password = "INSERT DATABASE PASSWORD"
sql_user = "INSERT DATABAESE NAME"
host = "INSERT HOST"
```

After creating the config.py file, the DataCollection.py Script can be run, due to rate limits the script will take a while to gather data.
Once data is gathered on a summoner, the user can be change by altering lines 31 and 32 to change the region or summoner's name.
```python

Region = "EUW1"
summonerName = "#####"

```
### Database ERD

![image](https://github.com/NathanSmallcalder/DataAnalysisLoL/assets/74361286/f3107797-aab2-463d-82e7-9ae17c2d9e1b)



