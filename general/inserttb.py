from createdb import databaseconnection
from showdb import showdatabases
from showtb import showtables

databases = showdatabases()
tables = showtables()

database = databases[0][0]
mydb = databaseconnection(database=database)


# def insertdatatable(tablename, data=None):
#     cursor = mydb.cursor()
#     try:
#         query = f"INSERT INTO {tablename} (StudentID, Name, Email, Contact) VALUES (%d, %s, %s, %d)"
#         val = [
#         (1,'Arjun', 'arjun@google.com', 9999988888),
#         (2,'Nimish', 'nimish@yahoo.com', 8888877777),
#         (3,'Yamini', 'yami@gamil.com', 7777766666),
#         (4,'Sachin', 'sachin@hotmail.com', 6666655555),
#         (5,'Shweta', 'shweta@hotmail.com', 5555544444)]
#         cursor.executemany(query, val)
#         mydb.commit()
#     except Exception as e:
#         print(e)

cursor = mydb.cursor()
query = f""" INSERT INTO Student VALUES (1,'Arjun', 'arjun@google.com', '9999988888'),
(2,'Nimish', 'nimish@yahoo.com', '8888877777'),
(3,'Yamini', 'yami@gamil.com', '7777766666'),
(4,'Sachin', 'sachin@hotmail.com', '6666655555'),
(5,'Shweta', 'shweta@hotmail.com', '5555544444')"""
# val = [
# ('Arjun', 'arjun@google.com', '9999988888'),
# ('Nimish', 'nimish@yahoo.com', '8888877777'),
# ('Yamini', 'yami@gamil.com', '7777766666'),
# ('Sachin', 'sachin@hotmail.com', '6666655555'),
# ('Shweta', 'shweta@hotmail.com', '5555544444')]
cursor.execute(query)
mydb.commit()

# if __name__ == "__main__":
    

    # student = tables[0][0]
    # insertdatatable(student)