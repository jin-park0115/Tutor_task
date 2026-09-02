# expense_challenge.py

import expense_service as service


def add_expense_cli():
    date = input("날짜 (예: 2026-09-03): ").strip()
    category = input("카테고리 (예: 식비, 교통): ").strip()
    description = input("내용 (예: 점심, 버스): ").strip()

    while True:
        amount_input = input("금액: ").strip()
        try:
            new_expense = service.create_expense(date, category, description, amount_input)
            break
        except ValueError as e:
            print(f"{e} 다시 시도합니다.")

    print(f"추가됨: {new_expense['date']} | {new_expense['category']} | "
          f"{new_expense['description']} | {new_expense['amount']}원\n")


def list_expenses_cli(expenses):
    if not expenses:
        print("등록된 지출이 없습니다.\n")
        return
    for e in expenses:
        print(f"{e['date']} | {e['category']} | {e['description']} | {e['amount']}원")
    print()


def total_expense_cli(expenses):
    total = service.get_total(expenses)
    print(f"총 지출: {total}원\n")


def print_menu():
    print("=== 지출 관리 ===")
    print("1. 지출 추가")
    print("2. 지출 목록 보기")
    print("3. 총 지출 보기")
    print("4. 새로고침 (DB에서 다시 불러오기)")
    print("5. 종료")


def main():
    expenses = service.get_all_expenses()

    while True:
        print_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_expense_cli()
            expenses = service.get_all_expenses()  # 추가 후 목록 갱신
        elif choice == "2":
            list_expenses_cli(expenses)
        elif choice == "3":
            total_expense_cli(expenses)
        elif choice == "4":
            expenses = service.get_all_expenses()
            print("새로고침 완료.\n")
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.\n")
            continue


if __name__ == "__main__":
    main()