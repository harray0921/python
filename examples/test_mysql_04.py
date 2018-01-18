import MySQLdb
db = MySQLdb.connect("localhost","root","ysq","address")
cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print "Database version: %s " % data

sql= """insert into employee(first_name,
        last_name,age,sex,income)
        value('Mac','Mohan',20,'M',2000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()


