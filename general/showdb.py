from createdb import databaseconnection


mydb = databaseconnection()


def showdatabases():
    cursor = mydb.cursor()
    databasenames = []
    try:
        cursor.execute("SHOW DATABASES")
        for databases in cursor:
            databases = list(databases)
            databasenames.append(databases)
            # print(databases)
    except Exception as e:
        print(e)

    else:
        return databasenames


if __name__ == "__main__":
    # query = "SHOW DATABASES"
    databases = showdatabases()
    print(databases)
