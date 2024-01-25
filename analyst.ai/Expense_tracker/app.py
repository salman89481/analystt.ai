from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# SQLite database configuration
DATABASE = "expenses.db"

def create_table():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        connection.commit()

@app.route('/')
def index():
    create_table()
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO expenses (amount, category, date)
            VALUES (?, ?, ?)
        """, (amount, category, date))
        connection.commit()

    return redirect(url_for('index'))

@app.route('/view_expenses')
def view_expenses():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        expenses = cursor.fetchall()

    return render_template('view_expenses.html', expenses=expenses)

if __name__ == '__main__':
    app.run(host="0.0.0.0")