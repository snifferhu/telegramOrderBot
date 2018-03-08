import logging, time

import pymysql

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='./log/access_{0}.log'.format(str(time.time())[:6]),
    filemode='a')


class DataBase(object):
    """docstring for DataBase"""

    def __init__(self, arg):
        super(DataBase, self).__init__()
        self.arg = arg

    def getConnect(self):
        # self.db = MySQLdb.connect(host='47.90.45.161',
        #                 user='gsmcdev',
        #                 passwd='Agsmc999*',
        #                 db='dtsc')
        self.db = pymysql.connect(host='47.90.45.161',
                                  user='gsmcdev',
                                  password='Agsmc999*',
                                  db='dtsc',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

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

# def main():
#     dataBase = DataBase('');
#     import time
#     print dataBase.query('select id from `order` where member_id = %s',[427009122])
#     for row in dataBase.query('select * from `order` where member_id = %s',[427009122]):
#         print row
#     print dataBase.insert('INSERT INTO `order` (`id`, `member_id`, `nick_name`, `price`, `item`) VALUES (%s,%s,%s,%s,%s)',[int(time.time()),427009122, 'Sniff', 160, 'A1 B1 C1'])
#
#
# if __name__ == '__main__':
#     main()
