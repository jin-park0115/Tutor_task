# expense_challenge.py (5단계: 전체 통합)
import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "expenses.csv"
FIELDNAMES = ["date", "category", "description", "amount"]


def load_expenses(path=DATA_PATH):
    try:
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            expenses = []
            for row in reader:
                row["amount"] = int(row["amount"])
                expenses.append(row)
            return expenses
    except FileNotFoundError:
        print(f"{path} 파일이 없습니다. 빈 목록으로 시작합니다.\n")
        return []


def save_expenses(expenses, path=DATA_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)
    print(f"{len(expenses)}건 저장 완료: {path}\n")


def add_expense(expenses):
    date = input("날짜 (예: 2026-09-03): ").strip()
    category = input("카테고리 (예: 식비, 교통): ").strip()
    description = input("내용 (예: 점심, 버스): ").strip()

    while True:
        amount_input = input("금액: ").strip()
        try:
            amount = int(amount_input)
            break
        except ValueError:
            print("숫자만 입력해주세요. 다시 시도합니다.")

    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    })
    print(f"추가됨: {date} | {category} | {description} | {amount}원\n")


def list_expenses(expenses):
    if not expenses:
        print("등록된 지출이 없습니다.\n")
        return

    for e in expenses:
        print(f"{e['date']} | {e['category']} | {e['description']} | {e['amount']}원")
    print()


def total_expense(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"총 지출: {total}원\n")
    return total


def print_menu():
    print("=== 지출 관리 ===")
    print("1. 지출 추가")
    print("2. 지출 목록 보기")
    print("3. 총 지출 보기")
    print("4. 저장하고 종료")
    print("5. 저장 안 하고 종료")


def main():
    expenses = load_expenses()

    while True:
        print_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("저장하고 종료합니다.")
            break
        elif choice == "5":
            print("저장하지 않고 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.\n")
            continue


if __name__ == "__main__":
    main()