import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='appclass')
mycursor = mydb.cursor()
mycursor.execute('select * from student')

result = mycursor.fetchone()
for i in result:
	print(i)