import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = 'TestDB1'
    )


# create table

cursor = mydb.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS TestDB1.Customer (Name VARCHAR(255), Address VARCHAR(255))""")


# insert multiple data into customer

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

# cursor.executemany(query, val)

# mydb.commit()

# print(cursor.rowcount, "was inserted.")

# select 

# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM TestDB1.Customer")
# result = cursor.fetchall()

# for x in result:
#   print(x)


# selecting columns
# cursor = mydb.cursor()

# cursor.execute("SELECT Name, Address FROM TestDB1.Customer")

# myresult = cursor.fetchall()

# for x in myresult:
#   print(x)


# one row
# cursor = mydb.cursor()

# cursor.execute("SELECT * FROM TestDB1.Customer")

# myresult = cursor.fetchone()

# print(myresult)

# where

# cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer WHERE Address='Khandwa 21/05'")
# result = cursor.fetchall()

# for x in result:
#   print(x)

# wildcard characters
# cursor.execute('SELECT DISTINCT Name, Address FROM TestDB1.Customer WHERE Address LIKE "%Kh%"')
# result = cursor.fetchall()

# for x in result:
#   print(x)

# orderby
# cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer ORDER BY Name")
# result = cursor.fetchall()
# for x in result:
#   print(x)

#orderby descending
cursor.execute("SELECT DISTINCT Name, Address FROM TestDB1.Customer ORDER BY Name DESC")
result = cursor.fetchall()
for x in result:
  print(x)
