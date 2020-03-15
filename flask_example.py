from flask import Flask

#Varible with name of application
app = Flask(__name__)

#create a starting point or root
# the "/" puts our data at the root of all routes
@app.route('/')

def hello_world():
    return 'Hello world'

#Why the hell is this "bit" not in the instructions? I lost a lot of time working this out.
app.run()