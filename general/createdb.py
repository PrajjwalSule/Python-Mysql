import mysql.connector

def databaseconnection(database=None):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = database
    )
    return mydb
 
# print(mydb)

mydb = databaseconnection()

def createdatabase(databasename):
    cursor = mydb.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {databasename}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    dbname = 'TestDB1'
    # query = f"CREATE DATABASE {dbname}"
    createdatabase(databasename=dbname)