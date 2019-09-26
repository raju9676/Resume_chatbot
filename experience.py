import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EXPERIENCE")

# Create table as per requirement
sql = """CREATE TABLE EXPERIENCE (
         ID INT ,         
         
         Company VARCHAR(15) ,
         Joiningdate VARCHAR(50),
         Enddate VARCHAR(50),
         Role VARCHAR(20)

          )"""

cursor.execute(sql)

# disconnect from server
db.close()
