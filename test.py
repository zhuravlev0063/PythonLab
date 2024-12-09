from flask import Flask, request, render_template, redirect, jsonify
import sqlite3
import json
import os

app = Flask(__name__)

# Инициализация базы данных
def setup_database():
    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_number TEXT NOT NULL UNIQUE,
        start_date DATE NOT NULL,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        case_id INTEGER NOT NULL,
        FOREIGN KEY (case_id) REFERENCES Cases(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_name TEXT NOT NULL,
        doc_type TEXT NOT NULL,
        upload_date DATE NOT NULL,
        case_id INTEGER NOT NULL,
        FOREIGN KEY (case_id) REFERENCES Cases(id)
    )
    """)

    conn.commit()
    conn.close()

setup_database()

# Главная страница с формами
@app.route("/")
def index():
    return render_template("index.html")

# Добавление нового дела
@app.route("/add_case", methods=["POST"])
def add_case():
    case_number = request.form["case_number"]
    start_date = request.form["start_date"]
    status = request.form["status"]

    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Cases (case_number, start_date, status)
    VALUES (?, ?, ?)
    """, (case_number, start_date, status))
    conn.commit()
    conn.close()

    return redirect("/")

# Просмотр дел
@app.route("/view_cases")
def view_cases():
    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cases")
    cases = cursor.fetchall()
    conn.close()

    return render_template("view_cases.html", cases=cases)

# Экспорт в JSON
@app.route("/export_json")
def export_json():
    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cases")
    cases = cursor.fetchall()
    conn.close()

    with open("cases.json", "w") as f:
        json.dump(cases, f)

    return "Экспорт выполнен! Файл cases.json создан."

# Импорт из JSON
@app.route("/import_json")
def import_json():
    if not os.path.exists("cases.json"):
        return "Файл cases.json не найден."

    with open("cases.json", "r") as f:
        cases = json.load(f)

    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Cases (id, case_number, start_date, status)
    VALUES (?, ?, ?, ?)
    """, cases)
    conn.commit()
    conn.close()

    return "Импорт выполнен! Данные добавлены в базу."

if __name__ == "__main__":
    app.run(debug=True)
