# db.py

import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
import psycopg2.extras

# db.py 위치: Tutor_task/chapter20/expense_challenge/db.py
# .env 위치 : Tutor_task/.env
# -> 3단계 위(parents[2])가 Tutor_task 루트
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_expenses():
    """전체 지출 목록을 list[dict]로 반환 (CSV 버전과 반환 형태 동일하게 유지)"""
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                "SELECT id, date, category, description, amount "
                "FROM expenses ORDER BY date"
            )
            rows = cur.fetchall()
            expenses = []
            for row in rows:
                row = dict(row)
                row["date"] = row["date"].isoformat()  # date 객체 -> "2026-09-01" 문자열
                expenses.append(row)
            return expenses
    finally:
        conn.close()


def add_expense(expense):
    """expense: {"date":..., "category":..., "description":..., "amount":...}"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO expenses (date, category, description, amount)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    expense["amount"],
                ),
            )
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    # 이 파일 단독 실행 시 연결 테스트
    print("env_path:", env_path, "exists:", env_path.exists())
    print("DB_CONFIG:", {**DB_CONFIG, "password": "***"})  # 비밀번호는 가려서 출력

    db.add_expense({
        "date": "2026-09-01",
        "category": "식비",
        "description": "테스트",
        "amount": 5000,
    }) if False else None  # 실수로 매번 추가되는 걸 막기 위해 기본은 비활성화

    print(load_expenses())