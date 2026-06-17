from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allows your API to be accessible across different origins

def get_db_connection():
    # Connects to the MariaDB database using the credentials we set up
    return mysql.connector.connect(
        host="localhost",
        user="web",
        password="webPass",
        database="student"
    )

@app.route("/")
def index():
    return "Welcome to the Student Database API!"

@app.route("/students")
def get_students():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True) # Returns rows as Python dictionaries
        
        # Query the table you built in Phase 3
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return jsonify(students) # Send the data back as JSON format
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run securely over port 8080 with your SSL certificates
    app.run(host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'privkey.pem'))
