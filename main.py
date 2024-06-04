#Initialization
from flask import *
import os

os.system('clear')
app = Flask(__name__)
port = 6536
host = "0.0.0.0"

#--------------------------------------------------------


#Defines what gets returned if user goes to url with just the / at the end.
@app.route('/')
#using the def function isn't actually needed but I like doing it for more complex flask websites.
def index():
	#This returns the template in /templates/index.html
	return render_template("index.html")


#This just sets the required params such as the host to run on and port to run on and if debug is on.
if __name__ == "__main__":
	app.run(host,port, debug=False)