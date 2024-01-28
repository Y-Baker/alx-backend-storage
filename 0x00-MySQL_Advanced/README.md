<div align="center">
  <img src="https://cdn.pixabay.com/photo/2013/07/12/17/22/database-152091_640.png" alt="python" width="80"/>
</div>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1000&size=34&pause=1000&width=435&lines=MySQL+Advanced)](https://git.io/typing-svg)

## Installation:
```bash
sudo apt update -y
sudo apt install mysql-server
sudo systemctl start mysql.service
```
<br />

## Configuring MySQL
- [Follow this instructions](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04#:~:text=Step%202%20%E2%80%94-,Configuring%20MySQL,-For%20fresh%20installations)
<br />

## Run MySQL Server
```bash
sudo service mysql start
mysql -u [user] -p
```
<br />

## How to import a SQL dump
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
<br />

## MySQL cheatsheet
- [Click here](https://devhints.io/mysql)

<br />

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
