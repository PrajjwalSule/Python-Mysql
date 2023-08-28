from createdb import databaseconnection
from showdb import showdatabases

# database = 'TestDB1'
databases = showdatabases()
mydb = databaseconnection(databases[0][0])


def showtables():
    cursor = mydb.cursor()
    tablesnames = []
    try:
        cursor.execute("SHOW TABLES")
        for tables in cursor:
            tables = list(tables)
            tablesnames.append(tables)
            # print(tables)
    except Exception as e:
        print(e)

    else:
        finaltable = []
        for i in tablesnames:
            finaltable.append(i)

        return finaltable



if __name__ == "__main__":
    # query = """ SHOW TABLES """
    tables = showtables()
    print(tables)