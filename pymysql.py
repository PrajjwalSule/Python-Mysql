import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = 'TestDB1'
    )


# create table

def createtable():
    cursor = mydb.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS TestDB1.Customer (Name VARCHAR(255), Address VARCHAR(255))""")


# insert multiple data into customer
def insertdata():
    cursor =  mydb.cursor()
    query = "INSERT INTO TestDB1.Customer (Name, Address) VALUES (%s, %s)"
    val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633'),
    ('Nimish', 'Khandwa 21/05'),
    ('Shweta', 'Bilaspur 105'),
    ('Sachin', 'Bhagalpur 210'),
    ('Uma', 'Kolkata 401'),
    ('Vaishali', 'Kanpur 12'),
    ('Soumya', 'Khargon 32'),
    ('Aakrit', 'Indore 123'),
    ('Vatsal', 'Bikhron 45'),
    ('Sujal', 'Janpaw Kuti 105')
    ]

    cursor.executemany(query, val)
    mydb.commit()
    print(cursor.rowcount, "was inserted.")

# select 

def getdata():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM TestDB1.Customer")
    result = cursor.fetchall()
    for x in result:
        print(x)


# selecting columns
def selectcolumns():
    cursor = mydb.cursor()
    cursor.execute("SELECT Name, Address FROM TestDB1.Customer")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


# one row
def onerow():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM TestDB1.Customer")
    myresult = cursor.fetchone()
    print(myresult)

# where
def where():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer WHERE Address='Khandwa 21/05'")
    result = cursor.fetchall()

    for x in result:
        print(x)

# wildcard characters
def wildcardcharacters():
    cursor = mydb.cursor()
    cursor.execute('SELECT DISTINCT Name, Address FROM TestDB1.Customer WHERE Address LIKE "%Kh%"')
    result = cursor.fetchall()

    for x in result:
        print(x)

# orderby
def orderby():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer ORDER BY Name")
    result = cursor.fetchall()
    for x in result:
        print(x)

#orderby descending
def orderbydesc():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer ORDER BY Name DESC")
    result = cursor.fetchall()
    for x in result:
        print(x)

#Delete

def deleterecord():
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM TestDB1.Customer WHERE Address='Main Road 989';")
    mydb.commit()

    print(cursor.rowcount, "record(s) deleted")

if __name__ == "__main__":
    pass
    # deleterecord()
