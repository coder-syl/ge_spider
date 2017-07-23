import pymysql
# from db_config import db_config as df
class db_conn:
    def __init__(self,host,port,user,pawd,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.pawd=pawd
        self.db=db
        self.charset=charset
        self.conn=self.db_cur()[0]
        self.cur=self.db_cur()[1]
    def db_cur(self):
        try:
            conn = pymysql.connect(host=self.host,port=self.port,
                                   user=self.user,password=self.pawd,
                                   database=self.db,charset=self.charset )
        except Exception as e:
            print("连接数据库出错")
            print(e)
        cur = conn.cursor()
        return conn,cur
    def db_select(self,sql):
        cur = self.db_cur()[1]
        try:
            cur.execute(sql)
            result=cur.fetchall()
            print('数据库操作成功')
        except Exception as e:
            print(e)
            print('数据库查询失败')
        return result
    def db_in_de_up_(self,sql):
        cur=self.db_cur()
        try:
            cur.execute(sql)
            print('数据库操作成功')
        except Exception as e:
            print(e)
            print('数据库操作失败')
    def db_close(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
            print('数据库关闭成功')
        except Exception as e:
            print(e)
            print('数据库关闭失败')

