from createdb import databaseconnection
from showdb import showdatabases

mydb = databaseconnection()
databasesnames = showdatabases()

def dropdatabase(databasename):
    cursor = mydb.cursor()
    try:
        cursor.execute(f"DROP DATABASE {databasename}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    dbname = databasesnames[0][0] # TestDB1
    # database = 'TestDB3'
    dropdatabase(dbname)
    # for i in databasesnames:
    #     print(i)
    
    # dbname = databasesnames[2][0]
    # print(dbname)