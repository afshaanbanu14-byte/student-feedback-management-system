from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="student_feedback"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor()

        query = """
            SELECT * FROM students
            WHERE email = %s
        """

        cursor.execute(query, (email,))
        student = cursor.fetchone()

        cursor.close()

        if student and check_password_hash(student[3], password):
            return "Login successful!"
        else:
            return "Invalid email or password!"

    return render_template("login.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        department = request.form["department"]
        year = request.form["year"]

        hashed_password = generate_password_hash(password)

        cursor = db.cursor()

        try:
            query = """
                INSERT INTO students (name, email, password, department, year)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (name, email, hashed_password, department, year)
            )

            db.commit()

            return "Registration successful!"

        except mysql.connector.Error:
            db.rollback()
            return "Email already registered or registration failed!"

        finally:
            cursor.close()

    return render_template("register.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        student_name = request.form["student_name"]
        subject = request.form["subject"]
        rating = request.form["rating"]
        comments = request.form["comments"]

        cursor = db.cursor()

        query = """
            INSERT INTO feedback (student_name, subject, rating, comments)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (student_name, subject, rating, comments)
        )

        db.commit()
        cursor.close()

        return "Feedback submitted successfully!"

    return render_template("feedback.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/admin")
def admin():
    cursor = db.cursor()

    query = "SELECT * FROM feedback"
    cursor.execute(query)

    feedbacks = cursor.fetchall()

    cursor.close()

    return render_template("admin.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)