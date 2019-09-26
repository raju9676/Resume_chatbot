import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS DETAILS")

# Create table as per requirement
sql = """CREATE TABLE DETAILS (
         ID INT  , 
         FIRSTNAME CHAR(20),
         LASTNAME CHAR(20),
         CITY CHAR(20),
         DOB VARCHAR(10),
         NUMBER VARCHAR(15)  ,
         SKILLS VARCHAR(50)
       )"""

cursor.execute(sql)

# disconnect from server
db.close()
