import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "sS123456%" )
#print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database Omkar")

#s = "create table Omkar.omkardetails(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
#q1 = cursor.execute(s)

q2 = cursor.execute("select * from Omkar.omkardetails")
print(q2)


