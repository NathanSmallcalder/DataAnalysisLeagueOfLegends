Setup MySQL

```
sudo docker pull mysql/mysql-server:latest

docker run --name=LeagueStats --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest

docker exec -it user_mysql_1 mysql -uroot -proot_password
```

To insert tables copy and paste the SQL script TableSetup.txt

Create a new ```config,py ``` with the following lines;

```python
api_key = "INSERT RIOT API KEY"
sql_password = "INSERT DATABASE PASSWORD"
sql_user = "INSERT DATABAESE NAME"
host = "INSERT HOST"

```

