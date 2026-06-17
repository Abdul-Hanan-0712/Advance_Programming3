from flask import Flask
app = Flask(__name__)

@app.route("/") # URL leading to method
def hello(): # Name of the method
    return("Hello World!") # Indented by 4 spaces

if __name__ == "__main__":
    # Added the closing parenthesis at the end here:
    app.run(host='0.0.0.0', port='8080', ssl_context=('cert.pem', 'privkey.pem'))
