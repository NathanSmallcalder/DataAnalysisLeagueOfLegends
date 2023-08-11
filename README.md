Setup MySQL

```
sudo docker pull mysql/mysql-server:latest

docker run --name LeagueStats -e MYSQL_ROOT_PASSWORD=password -d mysql

mysql -h 172.17.0.2 -P 3306 -u root -p
```

To insert tables copy and paste the SQL script TableSetup.txt

