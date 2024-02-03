<div align="center">
  <img src="https://1000logos.net/wp-content/uploads/2020/08/MongoDB-Logo.jpg" alt="storage" width="150"/>
</div>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1000&size=34&pause=1000&width=435&lines=NoSQL+MongoDB)](https://git.io/typing-svg)


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
- For more details [Follow this instructions](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
<br />

## Run Mongo shell
```bash
mongosh

echo "show dbs" | mongosh
```
<br />


## MongoDB cheatsheet
- [Click here](https://github.com/michaeltreat/Mongo_quickstart)

<br />

## Work With MongoDB in Python
```bash
pip3 install pymongo
```

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
