import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS SIGNUP")

# Create table as per requirement
sql = """CREATE TABLE SIGNUP (
         ID INT  AUTO_INCREMENT , 
         EMAIL VARCHAR(30) ,
         PASSWORD VARCHAR(15) ,
         PRIMARY KEY (ID,EMAIL)               
          )"""

cursor.execute(sql)

# disconnect from server
db.close()
