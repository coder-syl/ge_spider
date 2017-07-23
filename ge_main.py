from ge_get_url import (
get_url_from_db,
get_url_from_web
)
from ge_get_page import get_page_content
from gevent import monkey
monkey.patch_socket()
from gevent import pool
import gevent

def start():
    sql='select # from # where #'
    urls=get_url_from_db(sql)#获取url
    pool=gevent.pool.Pool(4)#设置并发度
    for url in urls:
        pool.add(gevent.spawn(get_page_content,url))
    pool.join()

start()
