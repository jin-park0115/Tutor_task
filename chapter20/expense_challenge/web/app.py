# web/app.py

from flask import Flask, jsonify, request, render_template
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import expense_service as service

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    return jsonify(service.get_all_expenses())


@app.route("/api/expenses", methods=["POST"])
def add_expense_api():
    data = request.get_json()

    try:
        new_expense = service.create_expense(
            data.get("date"),
            data.get("category"),
            data.get("description"),
            data.get("amount"),
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(new_expense), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)