import datetime
import mysql.connector

cnx = mysql.connector.connect(user='your user name',password='your password',host='your host', database='your database')
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM products "
         "WHERE name LIKE /'%DELL%'") #意思是DELL只要出現在字串裡就OK不管前後，如果是前後都有%的話

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for row in cursor:
    print(row['name'])

cursor.close()
cnx.close()
