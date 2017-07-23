from db import db_conn
from db_config import db_config as df
conn=db_conn(df['host'],df['port'],
            df['user'],df['password'],
            df['database'],df['charset'])
links=conn.db_select('select * from positions')
print(len(links))
conn.db_close()