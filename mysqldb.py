import MySQLdb
conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="mypython")
cursor = conn.cursor()
cursor.execute("select * from test")
row = cursor.fetchone()
print row[1]
cursor.close()
conn.close()
