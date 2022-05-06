import mysql.connector

my_db = mysql.connector.connect(host='localhost',
                                user='root',
                                password='Covington27!',
                                database='seasonal_users')
cursor = my_db.cursor()
# cursor.execute("CREATE DATABASE seasonal_users")
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)
# cursor.execute("USE seasonal_users") 

# cursor.execute("SHOW TABLES")
# for tb in cursor:
#     print(tb)
cursor.execute("SELECT * FROM usernames")
for x in cursor:
    print(x)
