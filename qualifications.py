import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS QUALIFICATIONS")

# Create table as per requirement
sql = """CREATE TABLE QUALIFICATIONS (
         ID INT   ,                 
         Tenthscore VARCHAR(5) ,
         Tenthschool VARCHAR(30),
         Tenthpassyear VARCHAR(12),
	 Interscore VARCHAR(5) ,
         Intercollege VARCHAR(30),
         InterDuration VARCHAR(12),
         UGscore VARCHAR(5),
         University VARCHAR(20),
         UGDuration VARCHAR(15)        
          )"""

cursor.execute(sql)

# disconnect from server
db.close()
