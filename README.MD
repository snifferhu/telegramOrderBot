**Telegram Order Bot**
-------------------------
Telegram Order Bot is a sample order robot.include order manage,balance manage,driver manage,restaurant manage sub-system.
It's focus quick order breakfast lunch and dinner.help drivers manage their income.

We are now collecting Telegram Order Bot user info in order to help us to improve Telegram Order Bot better, pls. kindly help us by providing yours xiaofei. who's using Telegram Order Bot, thanks :)

**OverView**
----------------------
- lib dependency
|lib |version|
|:-------------------|-----:|
|python | 3.6+|
|python telegram bot| 9.00|
|pymysql|0.8.0|

- database dependency
mysql 5.7+
or mariadb 10.0 Series+
**Feature schedule**
-------------------------
new commands 
- ship


change commands 


**Done Task**
-------------------------
|Task|Date|
|:------|--------------:|
|balance to bal|2018-3-9 17:44:33|
|cancel from single to multi play|2018-3-12 16:42:08|
|orderList to ol|2018-3-12 18:34:47|
|order|2018-3-13 13:37:39|
|balanceList to bl|2018-3-13 14:55:02|
|add inline callback button|2018-03-18 15:26:41|
|follow|2018-03-18 16:33:57|
|driver|2018-03-18 23:40:31|
|over|2018-03-19 01:47:24|
|feeList and fl|2018-03-21 15:00:24|
|f|2018-05-04 13:13:57|
|dep|2018-05-04 17:12:57|
|depositList|2018-5-11 10:37:35|
|dl|2018-5-11 10:37:38|
|search|2018-5-25 14:53:47|

**Install Step**
-------------------------
- python
```
1. download [python](https://www.python.org/downloads/) & install it
2. pip install pymysql
3. pip install python-telegram-bot
```
- database
```
1. download [mysql](https://www.mysql.com/downloads/) or [mariadb](https://mariadb.org/download/) & install it
2. unzip ./database/information_[*].zip
3. copy information_[*].sql & exec it
```
- file init
```
1. create log file 
2. create menu file
```
- config file context
file name : ./util/core_config.py
```python
# -*- coding: utf-8 -*-

db_config = {
    'user': '[your user name]',
    'password': '[your password]',
    'host': '127.0.0.1',
    'database': 'fate',
    # 'raise_on_warnings': True,
    # 'pool_name': "mypool",
    # 'pool_size': 5,
    # 'pool_reset_session': True,
}

robot_token = '[your bot token]'
```
- run
```bash
python main.py
```