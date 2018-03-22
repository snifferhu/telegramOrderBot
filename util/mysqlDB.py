import logging
import pymysql
from pymysql import OperationalError

from util.common import log_stream_handler

# 将定义好的console日志handler添加到root logger
logging.getLogger(__name__).addHandler(log_stream_handler())
logger = logging.getLogger(__name__)


class DataBase(object):
    """docstring for DataBase"""

    def __init__(self, host="172.0.0.1", user="root", port=3306,
                 password="123456", database="test"):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        # logger.info("host:%s,root:%s,port:%s,password:%s,db:%s", host, user, port, password, database)

    def getConnect(self):
        try:
            self.db = pymysql.connect(host=self._host,
                                      port=self._port,
                                      user=self._user,
                                      password=self._password,
                                      db=self._database,
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)
        except OperationalError as oe:
            logger.error("getConnect error :%s", oe)

    def query(self, sql, arg):
        self.getConnect()
        with self.db.cursor() as cursor:
            cursor.execute(sql, arg)
            result_date = cursor.fetchall()
            self.close()
            return result_date

    def execute(self, sql, arg):
        self.getConnect()
        with self.db.cursor() as cursor:
            cursor.execute(sql, arg)
            result_date = self.db.commit()
            self.close()
            return result_date

    def close(self):
        self.db.close()


def main():
    dataBase = DataBase(database='fate');
    import time
    print(dataBase.query('select id from `order` where member_id = %s', [427009122]))
    # for row in dataBase.query('select * from `order` where member_id = %s',[427009122]):
    #     print row
    # print dataBase.insert('INSERT INTO `order` (`id`, `member_id`, `nick_name`, `price`, `item`) VALUES (%s,%s,%s,%s,%s)',[int(time.time()),427009122, 'Sniff', 160, 'A1 B1 C1'])


if __name__ == '__main__':
    main()
