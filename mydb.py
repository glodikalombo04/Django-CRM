
import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password1234"
    )
    #creating /preparing a cursor object
    cursorObject = database.cursor()
    #create a database 
    cursorObject.execute("CREATE DATABASE aftech")


    print("Connection successful!")
    


except mysql.connector.Error as err:
    print(f"Error: {err}")
