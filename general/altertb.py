from createdb import databaseconnection
from showdb import showdatabases
from showtb import showtables

databases = showdatabases()
tables = showtables()

# TestDB2
database = databases[1][0]

mydb = databaseconnection(database)

def alteraddtable(tablename, updatecol):
    cursor = mydb.cursor()
    try:
        cursor.execute(f""" ALTER TABLE {tablename}
                                ADD {updatecol}
                            """)
    except Exception as e:
        print(e)

def alterdropcolumn(tablename, dropcol):
    cursor = mydb.cursor()
    try:
        cursor.execute(f""" ALTER TABLE {tablename}
                        DROP COLUMN {dropcol}
                        """)

    except Exception as e:
        print(e)

def altermodifycolumn(tablename, modifycol):
    cursor = mydb.cursor()
    try:
        cursor.execute(f""" ALTER TABLE {tablename}
                            MODIFY COLUMN {modifycol}
                        
                            """)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # TestTable1
    table = tables[0][0]
    # alteraddtable(table, 'Phone INT(20)')

    # alterdropcolumn(table, 'EMAIL')

    # altermodifycolumn(table, 'Age VARCHAR(10)')
 


