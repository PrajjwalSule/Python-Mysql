from createdb import databaseconnection
from showdb import showdatabases

databases = showdatabases()

# database = 'TestDB1'
database = databases[0][0]

mydb = databaseconnection(database)

def createtabledatabase(tablename, cols_datatypes):
    cursor = mydb.cursor()
    try:
        if len(cols_datatypes) == 5:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}(
                            {cols_datatypes[0]},
                            {cols_datatypes[1]},
                            {cols_datatypes[2]},
                            {cols_datatypes[3]},
                            {cols_datatypes[4]})
                            """)
        elif len(cols_datatypes) == 4:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}(
                            {cols_datatypes[0]},
                            {cols_datatypes[1]},
                            {cols_datatypes[2]},
                            {cols_datatypes[3]})
                            """)
        
        elif len(cols_datatypes) == 3:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}(
                            {cols_datatypes[0]},
                            {cols_datatypes[1]},
                            {cols_datatypes[2]})
                            """)
            
        elif len(cols_datatypes) == 2:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}(
                            {cols_datatypes[0]},
                            {cols_datatypes[1]})
                            """)
            
        else:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}(
                            {cols_datatypes[0]})
                            """)
    except Exception as e:
        print(e)

    
def createtablefromexistingone(newtablename, existedtablename, cols):
    cursor = mydb.cursor()
    try:
        if len(cols) == 5:
            cursor.execute(f""" CREATE TABLE IF NOT EXISTS {newtablename} AS
                                SELECT {cols[0]}, {cols[1]}, {cols[2]}, {cols[3]}, {cols[4]}
                                FROM {existedtablename}                  
                            
                        """)
        elif len(cols) == 4:
            cursor.execute(f""" CREATE TABLE IF NOT EXISTS {newtablename} AS
                                SELECT {cols[0]}, {cols[1]}, {cols[2]}, {cols[3]}
                                FROM {existedtablename}                  
                            
                        """)
            
        elif len(cols) == 3:
            cursor.execute(f""" CREATE TABLE IF NOT EXISTS {newtablename} AS
                                SELECT {cols[0]}, {cols[1]}, {cols[2]}
                                FROM {existedtablename}                  
                            
                        """)
        elif len(cols) == 2:
            cursor.execute(f""" CREATE TABLE IF NOT EXISTS {newtablename} AS
                                SELECT {cols[0]}, {cols[1]}
                                FROM {existedtablename}                  
                            
                        """)
            
        else:
            cursor.execute(f""" CREATE TABLE IF NOT EXISTS {newtablename} AS
                                SELECT {cols[0]}
                                FROM {existedtablename}                  
                            
                        """)
    except Exception as e:
        print(e)




if __name__ == "__main__":
    # tbname = 'TestTable1'
    # createtabledatabase(tbname, ['Name VARCHAR(30)', 'Age INT(10)', 'Email VARCHAR(50)'])

    # newtbname = 'TestTable2'
    # existingtable = 'TestTable1'
    # createtablefromexistingone(newtbname, existingtable, ['Name', 'Age'])

    tbname = 'Student'
    createtabledatabase(tbname, ['StudentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY',
                                 'Name VARCHAR(20)',
                                 'Email VARCHAR(20)',
                                 'Contact VARCHAR(20)',

    ])