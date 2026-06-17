from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!")
@app.route("/greetme")#different URL
def helloall(): # different method name
 name = request.args.get('name')#retrieve GET parameters
 return("Hello {}!".format(name))#Python’s string.format
if __name__ == "__main__":
    # Make sure this comment has 4 spaces before it
    app.run(host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'privkey.pem'))
