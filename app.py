import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="mywebsite"
)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO submissions (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    db.commit()
    cursor.close()

    return "✅ Submission successful!"

if __name__ == '__main__':
    app.run(debug=True)
