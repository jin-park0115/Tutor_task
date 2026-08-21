# 과제 A - 카페 주문 계산기

drink_name = input("음료 이름: ")
drintk_price = int(input("음료 가격: "))
drink_count = int(input("주문 수량: "))

total_drink = drintk_price * drink_count

print(f"주문하신 음료: {drink_name}, 총 금액: {total_drink}")