# expense_service.py
# CLI와 웹이 공통으로 쓰는 "순수 로직" 모듈.
# input()/print()/request/jsonify 같은 입출력 코드는 여기 넣지 않는다.

import db


def get_all_expenses():
    """DB에서 전체 지출 목록을 가져온다."""
    return db.load_expenses()


def create_expense(date, category, description, amount):
    """
    지출 한 건을 검증하고 DB에 저장한다.
    amount는 문자열이든 숫자든 받아서 여기서 int로 변환/검증한다.
    잘못된 값이면 ValueError를 그대로 던진다 (여기서 print하지 않음).
    호출하는 쪽(CLI/웹)이 자기 방식대로 에러를 보여준다.
    """
    try:
        amount = int(amount)
    except (ValueError, TypeError):
        raise ValueError("금액은 숫자여야 합니다.")

    if not date or not category:
        raise ValueError("날짜와 카테고리는 비어있을 수 없습니다.")

    new_expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }
    db.add_expense(new_expense)
    return new_expense


def get_total(expenses):
    """전체 합계 (list[dict] -> int)"""
    return sum(e["amount"] for e in expenses)


def get_category_totals(expenses):
    """카테고리별 합계 (list[dict] -> dict)"""
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals