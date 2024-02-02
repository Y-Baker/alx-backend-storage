<div align="center">
  <img src="https://cdn.pixabay.com/photo/2013/07/12/17/22/database-152091_640.png" alt="storage" width="80"/>
</div>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1000&size=34&pause=1000&width=435&lines=MySQL+Advanced)](https://git.io/typing-svg)


## Determine Ubuntu Version
```bash
cat /etc/lsb-release
```
<br />

## Installation:
```bash
sudo apt-get install gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

sudo apt-get update -y
sudo apt-get install -y mongodb-org

mongod --version
```
<br />

## Run MongoDB Server
```bash
mkdir -p ~/data/db

sudo service mongod start
sudo mongod --dbpath ~/data/db
```
- Connection should be on port 27017
- [Follow this instructions](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
<br />

## Run Mongo shell
```bash
mongosh
```
<br />


## MySQL cheatsheet
- [Click here](https://github.com/michaeltreat/Mongo_quickstart)

<br />

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
