from createdb import databaseconnection
from showtb import showtables
from showdb import showdatabases

# database = 'TestDB1'
databases = showdatabases()

mydb = databaseconnection(database=databases[0][0])
tables = showtables()


def droptable(tablename):
    """This will delete an entire table"""
    cursor = mydb.cursor()
    try:
        cursor.execute(f""" DROP TABLE {tablename}
             """)
    except Exception as e:
        print(e)


def truncatetable(tablename):
    """This will delete only data present in a table"""
    cursor = mydb.cursor()
    try:
        cursor.execute(f""" TRUNCATE TABLE {tablename}
            """)
    except Exception as e:
        print(e)

    
if __name__ == "__main__":
    tablename = tables[0][0] # TestTable1
    truncatetable(tablename)

    tablename2 = tables[1][0] # TestTable2
    droptable(tablename2)

