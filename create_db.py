import mysql.connector

my_db = mysql.connector.connect(host='localhost',
                                user='root',
                                passwd='Covington27!')
cursor = my_db.cursor()
# cursor.execute("CREATE DATABASE seasonal_users")
cursor.execute("SHOW DATABASES")
cursor.execute("USE seasonal_users") 
