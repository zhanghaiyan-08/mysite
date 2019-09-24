__author__ = 'Supi'
# @Time    : 2018/8/17 8:40
import pymysql
import Data.Common.environment as environment
enviroment='master'
dburl = environment.enviroment(enviroment)[0]
#打开数据库
def open_MySQL():
    global cur,conn
    if enviroment in ['test','master']:
        conn = pymysql.connect(host='sh-cdb-iop8kxmv.sql.tencentcdb.com', port=63504, user='qiyunservicetest', passwd='kjasdoIKHDAen7gd', db=dburl)
    else:
        print('环境名称错误')
    cur = conn.cursor()   # 使用cursor()方法获取操作游标

#查询语句
def get_MySQLselect(selectcode):
    cur.execute("%s " %  (selectcode))
    result = cur.fetchall()
    conn.commit()
    return result

#插入语句
def get_MySQLinsert():
    cur.execute("insert into table_name(xh,name,link,notes) VALUES (2,'office','3','4')")  # 使用execute方法执行SQL语句
    result = cur.fetchall()   # 使用 fetchall() 方法获取数据
    conn.commit()    # 提交到数据库执行
    return result

#删除语句
def get_MySQLdelete(deletecode):
    cur.execute("%s " %  (deletecode))
    result = cur.fetchall()
    conn.commit()    #提交修改
    return result

#关闭数据库
def close_MySQL():
    cur.close()
    conn.close()




'''

s = open_MySQL()
s1 = get_MySQLselect("select count(*) from org_orgrelation  where CustomerID='d0f26025-7278-4a21-b09a-71009b46d1f2' AND (state = 4)")
print(s1)
s2 = close_MySQL()




try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
   '''