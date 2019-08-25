import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="webstore"
    )
except mysql.connector.Error as err:
    print("Err")
