# --------------------------------- TO CREATE RESUME CHATBOT USING DIALOGFLOW WEBHOOK -------------------------------- #

import os
from flask import Flask
from flask import request
from flask import make_response
import re
import json
import MySQLdb

app = Flask(__name__)

# Open database connection
db = MySQLdb.connect(host='localhost',
                    database='db',
                    user='root',
                    password='1234',
                    )      
# prepare a cursor object using cursor() method
cursor =db.cursor()
   
@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    print(json.dumps(req,indent=4))
    res = webHookResult(req)
    res = json.dumps(res,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    return r

def webHookResult(req):    
    #### ------------------------ ACTIONS -------------------------------- ####

    if req.get("queryResult").get("action") == "email" :
       f=signup(req)
       return(f)
    if req.get("queryResult").get("action") == "pin" :
       f=pin(req)
       return(f)
    if req.get("queryResult").get("action") == "existemail" :
       f=existemail(req)
       return(f)
    if req.get("queryResult").get("action") == "password" :
       f=password(req)
       return(f)
    if req.get("queryResult").get("action") == "existpin" :
       f=existpin(req)
       return(f)
    if req.get("queryResult").get("action") == "details":
       f=details(req)
       return(f)
    if req.get("queryResult").get("action") == "updatedetails":
       f=updatedetails(req)
       return(f)    
    if req.get("queryResult").get("action") == "tenthqualification":
       f=tenthqualification(req)
       return(f)  
    if req.get("queryResult").get("action") == "tenthschool":
       f=tenthschool(req)
       return(f)

    if req.get("queryResult").get("action") == "interqualification":
       f=interqualification(req)
       return(f)
    if req.get("queryResult").get("action") == "intercollege":
       f=intercollege(req)
       return(f)    
    if req.get("queryResult").get("action") == "ugqualification":
       f=ugqualification(req)
       return(f)
    if req.get("queryResult").get("action") == "university":
       f=university(req)
       return(f)
    if req.get("queryResult").get("action") == "updatetenthqualification":
       f=updatetenthqualification(req)
       return(f)
    if req.get("queryResult").get("action") == "updatetenthschool": 
       f=updatetenthschool(req)
       return(f)
    if req.get("queryResult").get("action") == "updateinterqualification":
       f=updateinterqualification(req)
       return(f)      
    if req.get("queryResult").get("action") == "updateintercollege":
       f=updateintercollege(req)
       return(f)
    if req.get("queryResult").get("action") == "updateugqualification":
       f=updateugqualification(req)
       return(f)
    if req.get("queryResult").get("action") == "updateuniversity":
       f=updateuniversity(req)
       return(f)
    if req.get("queryResult").get("action") == "experience":
       f=experience(req)
       
    if req.get("queryResult").get("action") == "project":
       f=project(req)

    

          # --------------------------------- SIGNUP -------------------------------------------#
def signup(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    email = parameters.get("email")
    print(email)
    
    sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
    cursor.execute(sql)
    
    myresult = cursor.fetchone()    # fetch the first row only
    print(myresult)
    if myresult is None:
          speech="please set your pin "
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }  
       
    else :
          speech="you are an  already existing customer . Have you remembered your pin ? (YES/NO)"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }       


    # --------------------------------- SET PIN OR PASSWORD -------------------------------------------#
def pin(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       password = parameters.get("pin")
       email = parameters.get("email")       
       print(email,password)
  
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       cursor.execute(sql)
       myresult = cursor.fetchone()
       print(myresult)
       
       if myresult is None:
          cursor.execute("INSERT INTO SIGNUP (EMAIL,PASSWORD) VALUES(%s,%s)",(email,password))
          db.commit()
         
          speech="please enter your skills"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }  
       else :
          speech="you email id is already existed please login with your email id and pin"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }     


    # --------------------------------- LOGIN -------------------------------------------#       
def existemail(req):
       result = req.get("queryResult")     
       parameters = result.get("parameters")
       email = parameters.get("email")
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       cursor.execute(sql)
       myresult = cursor.fetchone()
       print(myresult)
       
       if myresult is None:
          speech=" Account with this email id does not exist . Do you like to create new account (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="please enter your pin or password"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }  
 

    # --------------------------------- PASSWORD -------------------------------------------#         
def password(req):
       result = req.get("queryResult")
      
       parameters = result.get("parameters")
       email = parameters.get("email")
       password = parameters.get("password")
       sql="SELECT PASSWORD FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       cursor.execute(sql)
       myresult = cursor.fetchone()
       print(myresult) 
       if password==myresult[0]:
          speech=" Which details would you like to update 1.Personal details 2.Qualifications 3.Experience 4.Projects 5.Exit"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
           speech=" Entered pin is not matched to your login pin . do yo know your password (YES/NO)?"
           return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
           }         


    # --------------------------------- EXISTPIN -------------------------------------------#
def existpin(req):
       result = req.get("queryResult")     
       parameters = result.get("parameters")
       email = parameters.get("email")
       password = parameters.get("password")
       print(password)
       
       sql="SELECT PASSWORD FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       cursor.execute(sql)
       myresult = cursor.fetchone()
       print(myresult) 
       if password==myresult[0]:
          speech=" Which details would you like to update 1.Personal details 2.Qualifications 3.Experience 4.Projects 5.Exit"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
           speech=" Entered pin is not matched to your login pin . do yo know your password (YES/NO)?"
           return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
           }         


    # --------------------------------- DETAILS -------------------------------------------#
def details(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
      
       firstname=parameters.get("fname")
       lastname=parameters.get("lname")
       city=parameters.get("city")
       
       dob = parameters.get("dob")
       number = parameters.get("number") 
       skills=parameters.get("skills")
       email = parameters.get("email")
       print(dob,number,firstname,lastname,skills,city,email)
       
              
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       cursor.execute("INSERT INTO DETAILS (ID,FIRSTNAME,LASTNAME,CITY,DOB,NUMBER,SKILLS) VALUES(%s,%s,%s,%s,%s,%s,%s)",(a,firstname,lastname,city,dob,number,skills))
      
  
       db.commit()
       speech="please enter your tenth standard marks in percentage(Example : 90% or 76%)"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       }    
 

    # --------------------------------- UPDATE DETAILS -------------------------------------------#      
def updatedetails(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
 
       firstname=parameters.get("fname")
       lastname=parameters.get("lname")
       city=parameters.get("city")
       
       dob = parameters.get("dob")
       number = parameters.get("number") 
       skills=parameters.get("skills")
       email = parameters.get("email")
       print(dob,number,firstname,lastname,skills,city,email)
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])

       sql="SELECT * FROM DETAILS WHERE ID=\""+a+"\""
       
       cursor.execute(sql)
       record= cursor.fetchone()
       print(record)        
       
       if record is None:
          sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\""
          print("SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\"")
          cursor.execute(sql)
          record= cursor.fetchone()
          e=record[1]
          i=record[0]
          i=str(i)
          cursor.execute("INSERT INTO DETAILS (ID,FIRSTNAME,LASTNAME,CITY,DOB,NUMBER,SKILLS) VALUES(%s,%s,%s,%s,%s,%s,%s)",(i,firstname,lastname,city,dob,number,skills)) 
          db.commit()
          speech="Which details would you like to update 1.Personal details 2.Qualifications 3.Experience 4.Projects 5.Exit"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          } 
       else :     
          sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\""
          print("SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\"")
          cursor.execute(sql)
          record= cursor.fetchone()
          e=record[1]
          i=record[0]
          i=str(i)
          sql1="DELETE FROM DETAILS WHERE ID=\""+ i +"\""
          print("DELETE FROM DETAILS WHERE ID=\""+ i +"\"")
          cursor.execute(sql1)
          db.commit()
          print(e,i,record)
        
          cursor.execute("INSERT INTO DETAILS (ID,FIRSTNAME,LASTNAME,CITY,DOB,NUMBER,SKILLS) VALUES(%s,%s,%s,%s,%s,%s,%s)",(i,firstname,lastname,city,dob,number,skills))
          print("INSERT INTO DETAILS (ID,FIRSTNAME,LASTNAME,CITY,DOB,NUMBER,SKILLS) VALUES(%s,%s,%s,%s,%s,%s,%s)",(i,firstname,lastname,city,dob,number,skills)) 
          db.commit()
          speech="Which details would you like to update 1.Personal details 2.Qualifications 3.Experience 4.Projects 5.Exit"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }    
  

    # --------------------------------- TENTH QUALIFICATION -------------------------------------------#
def tenthqualification(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Tenthscore = parameters.get("Tenthpercentage")
       print(Tenthscore)
       type(Tenthscore)
       num = re.sub(r'\D', "", Tenthscore)
       num1=int(num)

       email = parameters.get("email")
       print(Tenthscore)
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your school name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }


    # --------------------------------- TENTH SCHOOL -------------------------------------------#
def tenthschool(req):    
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Tenthscore = parameters.get("Tenthpercentage")
       tenthschool=parameters.get("tenthschool")
       tenthpassyear=parameters.get("tenthpassyear")
       email = parameters.get("email")
       print(Tenthscore)
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       tenthpassyear=str(tenthpassyear)
       cursor.execute("INSERT INTO QUALIFICATIONS (ID,Tenthscore,Tenthschool, Tenthpassyear,Interscore, Intercollege,InterDuration, UGscore,University,UGDuration) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,Tenthscore,tenthschool, tenthpassyear,0,0,0,0,0,0))
       db.commit()
       speech="please enter your Inter score in percentage(Example : 90% or 76%)"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       } 


    # --------------------------------- INTERMEDIATE QUALIFICATIONS -------------------------------------------#
def interqualification(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Interpercentage = parameters.get("Interpercentage")
       num = re.sub(r'\D', "", Interpercentage)
       num1=int(num)

       email = parameters.get("email")
       
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your Inter college name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
 
    # ---------------------------------- INTERMEDIATE COLLEGE -------------------------------------------#   
def intercollege(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Interpercentage = parameters.get("Interpercentage")
       intercollege=parameters.get("intercollege")
       interpassyear=parameters.get("interpassyear")
       email = parameters.get("email")
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       interpassyear=str(interpassyear)
       sql="UPDATE QUALIFICATIONS SET  Interscore=\"" + Interpercentage + "\" , Intercollege=\"" + intercollege + "\", InterDuration=\"" + interpassyear + "\"  WHERE ID=\""+ a + "\""
       cursor.execute(sql)
       db.commit()
       speech="please enter your Under graduation score in percentage(Example : 90% or 76%)"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       }   


    # --------------------------------- UNDER GRADUATION QUALIFICATIONS -------------------------------------------#
def ugqualification(req):    
       result = req.get("queryResult")
       parameters = result.get("parameters")
       ugpercentage= parameters.get("UGpercentage")
       num = re.sub(r'\D', "", ugpercentage)
       num1=int(num)

       email = parameters.get("email")
       
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your University name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }


    # --------------------------------- UNIVERSITY -------------------------------------------#    
def university(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       ugpercentage = parameters.get("UGpercentage")
       university=parameters.get("university")
       ugpassyear=parameters.get("ugpassyear")
       email = parameters.get("email")
      
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       ugpassyear=str(ugpassyear)
       sql="UPDATE QUALIFICATIONS SET  UGscore=\"" + ugpercentage + "\" , University=\"" + university + "\", UGDuration=\"" + ugpassyear + "\"  WHERE ID=\""+ a + "\""
       cursor.execute(sql)
       db.commit()
       speech="Do you have experience? (Yes/No)"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       } 
    
 
    # --------------------------------- UPDATE TENTH QUALIFICATIONS -------------------------------------------#
def updatetenthqualification(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Tenthpercentage = parameters.get("Tenthpercentage")
       
       num = re.sub(r'\D', "", Tenthpercentage)
       num1=int(num)

       email = parameters.get("email")
       
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your school name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }


    # --------------------------------- UPDATE TENTH SCHOOL -------------------------------------------#    
def updatetenthschool(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Tenthpercentage = parameters.get("Tenthpercentage")
       tenthschool=parameters.get("tenthschool")
       tenthpassyear=parameters.get("tenthpassyear")
       email = parameters.get("email")
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0],a)
       
       sql="SELECT * FROM QUALIFICATIONS WHERE ID=\""+a+"\""
       
       cursor.execute(sql)
       record= cursor.fetchone()
       print(record)        
       if record is None:
          sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\""
          print("SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\"")
          cursor.execute(sql)
          record= cursor.fetchone()
          e=record[1]
          i=record[0]
          i=str(i)
          cursor.execute("INSERT INTO QUALIFICATIONS (ID,Tenthscore,Tenthschool, Tenthpassyear,Interscore, Intercollege,InterDuration, UGscore,University,UGDuration) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,Tenthpercentage,tenthschool, tenthpassyear,0,0,0,0,0,0))
          db.commit()
          speech="please enter your Inter score in percentage(Example : 90% or 76%)"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          } 
       else :     
          sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\""
          print("SELECT * FROM SIGNUP WHERE EMAIL=\""+email+"\"")
          cursor.execute(sql)
          record= cursor.fetchone()
          e=record[1]
          a=record[0]
          a=str(a)
          sql1="DELETE FROM QUALIFICATIONS WHERE ID=\""+ a +"\""
          print("DELETE FROM QUALIFICATIONS WHERE ID=\""+ a +"\"")
          cursor.execute(sql1)
          db.commit()
          
          cursor.execute("INSERT INTO QUALIFICATIONS (ID,Tenthscore,Tenthschool, Tenthpassyear,Interscore, Intercollege,InterDuration, UGscore,University,UGDuration) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,Tenthpercentage,tenthschool, tenthpassyear,0,0,0,0,0,0))
         
  
          db.commit()
          speech="please enter your Inter score in percentage(Example : 90% or 76%)"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }    
 

    # --------------------------------- UPDATE INTERMEDIATE QUALIFICATIONS -------------------------------------------#      
def updateinterqualification(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Interpercentage = parameters.get("Interpercentage")
       num = re.sub(r'\D', "", Interpercentage)
       num1=int(num)

       email = parameters.get("email")
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your Inter college name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }  
      

    # --------------------------------- UPDATE INTERMEDIATE COLLEGE -------------------------------------------#                
def updateintercollege(req):    
       result = req.get("queryResult")
       parameters = result.get("parameters")
       Interpercentage = parameters.get("Interpercentage")
       intercollege=parameters.get("intercollege")
       interpassyear=parameters.get("interpassyear")
       email = parameters.get("email")
       Interpercentage=str(Interpercentage)
       interpassyear=str(interpassyear)
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       
       sql="SELECT * FROM DETAILS WHERE ID=\""+a+"\""
       
       cursor.execute(sql)
       record= cursor.fetchone()
       print(record)        
       sql="UPDATE QUALIFICATIONS SET  Interscore=\"" + Interpercentage + "\" , Intercollege=\"" + intercollege + "\", InterDuration=\"" + interpassyear + "\"  WHERE ID=\""+ a + "\""
       cursor.execute(sql)
       db.commit()
       speech="please enter your Under graduation score in percentage(Example : 90% or 76%)"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       } 
      
          
    # --------------------------------- UPDATE UNDER GRADUATION QUALIFICATIONS -------------------------------------------#    
def updateugqualification(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       ugpercentage= parameters.get("UGpercentage")
       num = re.sub(r'\D', "", ugpercentage)
       num1=int(num)

       email = parameters.get("email")
       
       if num1>100:
          speech="you have entered wrong percentage that is more than 100.would you like to reenter your percentage (YES/NO) ?"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }
       else :
          speech="Please enter your University name"
          return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
          }


    # --------------------------------- UPDATE UNIVERSITY -------------------------------------------#       
def updateuniversity(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       ugpercentage = parameters.get("UGpercentage")
       university=parameters.get("university")
       ugpassyear=parameters.get("ugpassyear")
       email = parameters.get("email")
       ugpassyear=str(ugpassyear)
       
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       
       sql="SELECT * FROM DETAILS WHERE ID=\""+a+"\""
       
       cursor.execute(sql)
       record= cursor.fetchone()
      
       sql="UPDATE QUALIFICATIONS SET  UGscore=\"" + ugpercentage + "\" , University=\"" + university + "\", UGDuration=\"" + ugpassyear + "\"  WHERE ID=\""+ a + "\""
       cursor.execute(sql)
       db.commit()
       speech="Which details would you like to update 1.Personal details 2.Qualifications 3.Experience 4.Projects 5.Exit"
       return {
                'fulfillmentText':speech,
                'displayText':speech,
                'source':'dialogflow'
       } 
       
     


    # --------------------------------- EXPERIENCE -------------------------------------------#   
def experience(req):
       result = req.get("queryResult")
       parameters = result.get("parameters")
       
       cname=parameters.get("cname") 
       startdate=parameters.get("startdate")
       role=parameters.get("role")
       email = parameters.get("email")
       enddate=parameters.get("enddate")
       start=re.sub("T.*$", "", startdate)
       print(start)
       end=re.sub("T.*$", "", enddate)
       print(end)
    
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       cursor.execute("INSERT INTO EXPERIENCE VALUES(%s,%s,%s,%s,%s)" ,(a,cname,start,end,role))
       db.commit() 


    # --------------------------------- PROJECT DETAILS -------------------------------------------#   
def project(req):   
       result = req.get("queryResult")
       parameters = result.get("parameters")
       
       ProjectTitle=parameters.get("projecttitle") 
       Projectdescription=parameters.get("projectdescription")
       email = parameters.get("email")
      
       sql="SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\""
       print("SELECT * FROM SIGNUP WHERE EMAIL=\""+ email + "\"")
       cursor.execute(sql)
       myresult = cursor.fetchone()
       a=myresult[0]
       a=str(a)
       print(myresult[0])
       cursor.execute("INSERT INTO PROJECTS VALUES(%s,%s,%s)" ,(a,ProjectTitle,Projectdescription))
       db.commit()  


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')




