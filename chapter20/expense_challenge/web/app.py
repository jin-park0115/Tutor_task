# web/app.py

from flask import Flask, jsonify, request, render_template
from pathlib import Path
import csv

app = Flask(__name__)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "expenses.csv"
FIELDNAMES = ["date", "category", "description", "amount"]


def load_expenses():
    try:
        with open(DATA_PATH, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            expenses = []
            for row in reader:
                row["amount"] = int(row["amount"])
                expenses.append(row)
            return expenses
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    expenses = load_expenses()
    return jsonify(expenses)


@app.route("/api/expenses", methods=["POST"])
def add_expense_api():
    data = request.get_json()

    # 최소한의 검증 (input()의 try/except를 대체하는 역할)
    try:
        amount = int(data["amount"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "amount는 숫자여야 합니다."}), 400

    new_expense = {
        "date": data.get("date", ""),
        "category": data.get("category", ""),
        "description": data.get("description", ""),
        "amount": amount,
    }

    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)

    return jsonify(new_expense), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)