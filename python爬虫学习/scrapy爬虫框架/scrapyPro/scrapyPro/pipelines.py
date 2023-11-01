# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class ScrapyproPipeline:
    #重写父类的方法，该方法只被第一次的时候被调用
    fp = None
    def open_spider(self,spider):
        print('开始爬虫.......')
        self.fp = open('./bossZhiPin.txt','w',encoding='utf-8')

    #每接收一次item 都会调用一次
    def process_item(self, item, spider):
        name = item['name']
        pay = item['pay']
        self.fp.write(name+':'+pay+'\n')
        return item
    def close_spider(self,spider):
        print('关闭爬虫通道')
        self.fp.close()

class mysqlPileLine(object):
    conn = None
    cursor = None
    #连接数据库
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='ldx12138',database='bossZhiPin')
        print("self.conn ====",self.conn)
        self.cursor = self.conn.cursor()
        #创建数据库表
        # sql = "CREATE TABLE user(runoob_id INT NOT NULL AUTO_INCREMENT,name VARCHAR(100) NOT NULL,pay VARCHAR(100) NOT NULL,submission_date DATE,PRIMARY KEY ( runoob_id ))ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        # self.cursor.execute(sql)
        # self.conn.commit()
        #创建新的数据库
        # self.cursor.execute('CREATE DATABASE bossZhiPin')
        #删除数据库表
        # self.cursor.execute('DROP TABLE user')

        print("self.cursor ======== ",self.cursor)
    #每接收一次item 都会调用一次clea
    def process_item(self, item, spider):
        try:
            sql = 'insert into user(pay,name) values(%s,%s)'
            content = (item["pay"],item["name"])
            self.cursor.execute(sql,content) 
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        print('关闭爬虫通道11111')
        self.conn.close()
        self.cursor.close()