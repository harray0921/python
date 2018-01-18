import MySQLdb
db = MySQLdb.connect("localhost","root","ysq","address")
cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print "Database version: %s " % data

cursor.execute("drop table if exists employee")
sql= """create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rpllback()

db.close()


