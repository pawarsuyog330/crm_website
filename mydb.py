import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("Database Created")
