from db import db_conn
from db_config import db_config as df
def get_url_from_db(sql):
    conn=db_conn(df['host'],df['port'],
                df['user'],df['password'],
                df['database'],df['charset'])
    links=conn.db_select(sql)
    url_list=[]
    for link in links:
        url_list.append(link)
    return url_list
    conn.db_close()
def get_url_from_web():
    pass