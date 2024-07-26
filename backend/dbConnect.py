import mysql.connector

myBD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iarowosola9876#+",
    database="",
    auth_plugin='mysql_native_password'
)


myCursor = myBD.cursor()
# print("connected")

# create database 
myCursor.execute("CREATE DATABASE arcade_db")
print("Database Created...")

# superuser details...
# username - arcade
# password - arcade2024
# mail - iarowosola25@gmail.com 