from createdb import databaseconnection
from showdb import showdatabases
from showtb import showtables

databases = showdatabases()
tables = showtables()

database = databases[0][0]
mydb = databaseconnection(database=database)

def describetable(tablename):
    cursor = mydb.cursor()
    try:
        cursor.execute(f"DESC {tablename}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    student = tables[0][0]
    describetable(student)