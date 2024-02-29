<div align="center">
  <img src="https://ps.w.org/redis-cache/assets/banner-1544x500.png?rev=2315420" alt="redis" width="150"/>
</div>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1000&size=34&pause=1000&width=435&lines=Redis+Basic)](https://git.io/typing-svg)


## Determine Ubuntu Version
```bash
cat /etc/lsb-release
```
<br />

## Installation:
```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg


echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update -y
sudo apt-get install redis

redis-server --version
redis-cli --version
```
<br />

## Run Redis Server
```bash
sudo service redis-server start
```
- Connection should be on port 6379
- For more details [Follow this instructions](https://redis.io/docs/install/install-redis/install-redis-on-windows/)
<br />

## Run redis shell
```bash
redis-cli
```
<br />


## Redis Command cheatsheet
- [Click here](https://redis.io/commands/)

<br />

## Work With Redis in Python
```bash
pip3 install redis
```
<br />

## Quickly connecting to redis in Python
```python
import redis
r = redis.Redis()
# r = redis.Redis(host='foo.bar.com', port=12345) # IF you want to use custom host or port
r.ping()
```
## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
