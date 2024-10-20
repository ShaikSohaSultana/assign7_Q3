from flask import Flask, render_template, request, redirect, flash
import mysql.connector


app = Flask(__name__)
app.secret_key = "your_secret_key"

# Configure MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="registration_db"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['user_id']
    mobile_number = request.form['mobile_number']
    password = request.form['password']

    if not user_id or not mobile_number or not password:
        flash('All fields are required!', 'error')
        return redirect('/')

    cursor = db.cursor()
    query = "INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)"
    values = (user_id, mobile_number, password)

    try:
        cursor.execute(query, values)
        db.commit()
        flash('Registration successful!', 'success')
    except mysql.connector.Error as err:
        db.rollback()
        flash(f"Error: {err}", 'error')

    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
