import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS PROJECTS")

# Create table as per requirement
sql = """CREATE TABLE PROJECTS (
         ID INT,                 
         ProjectTitle VARCHAR(20),
         Projectdescription VARCHAR(40)
        
          )"""

cursor.execute(sql)

# disconnect from server
db.close()
