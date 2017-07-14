#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3307,
        user='root',
        passwd='test',
        db ='test',
        charset='utf8'
        )
cur = conn.cursor()

# #一次插入多条记录
# sqli="insert into honey3(first_name,last_name,age,sex,income) values ('%r', '%r', '%r', '%r', '%r') "
# cur.executemany(sqli,[
#     ('737c', 'M477an', 21, 'M', 2010),
#     ('77447c', '377an', 22, 'M', 2100),
#     ('7755657c', '1777an', 23, 'M', 900),
#     ])
#
#
#
# 创建数据表
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

# # 插入一条数据
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


# # 修改查询条件的数据
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# 删除查询条件的数据
# cur.execute("delete from student where age='9'")
# aa=cur.execute("select * from honey3")
# print aa

#插入一条数据
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

#一次插入多条记录
sqli="insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),
    ])

cur.close()
conn.commit()
conn.close()