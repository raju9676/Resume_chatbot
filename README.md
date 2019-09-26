## implementation procedure
Visit https://dialogflow.com/
Login with any gmail account
Create 'Resume_chatbot' named agent and train intents,
Install ngrok , flask , mysql and  mysqldb on your terminal(ubuntu),(or)we can install all set in windows also,
In new terminal type command  "ngrok http 80" to get the link, 
"80" This is prot address in your local host it can be any integer value,
Ngrok proved a url,take that url and paste that url in the fullfillment section in dailogflow for establishing webhook connection,
Example of url to be paste in fullfillment is : https://ea49fba8.ngrok.io,
Add "/webhook" to the url in fullfillment its looks like this : https://ea49fba8.ngrok.io/webhook,
We can run this files in virtuval enviroment,
In new terminal type command "FLASK_APP=filename.py flask run",
In mysql create database ,needed tables for the resume_chatbot...
## attributes define
# Dialogflow
1.Dialogflow is a Google proveding AI based chatbot platform
2.it is a interaction technologies based on natural language conversations.
# Flask
1.Flask is a web application framework written in Python.
# Ngrok
1.its a tool that creates a secure tunnel on your local machine
2.along with a public URL you can use for browsing your local site.
# MySQLdb 
MySQLdb is an thread-compatible interface to the popular MySQL
database server that provides the Python database API.
# Tools required for this project:
1. Flask (web framework)
2. Mysql,Postgressql (database)
3. MySQLdb,Psycgp2
4. Sublime text or Text editor
# Environment :
1. Ubuntu 
2. Python
# Other utilities :
1. Dialogflow account
2. Ngrok
