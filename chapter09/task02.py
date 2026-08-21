# 과제 B - 쇼핑 할인 프로그램

total_price = int(input("총 주문 금액: "))

if total_price >= 100000:
    discount_rate = 0.1
    print("10% 할인을 받았습니다.")
elif(total_price >= 50000):
    discount_rate = 0.05
    print("5% 할인을 받았습니다.")
else:
    discount_rate = 0
    print("No discount")

discount_price = int(total_price * discount_rate)
final_price = total_price - discount_price

print(f"할인 금액: {discount_price}원")
print(f"최종 결제 금액: {final_price}원")