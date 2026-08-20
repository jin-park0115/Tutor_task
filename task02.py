# 과제 A. 카페 주문 금액
coffe_price = 4500
cake_price = 6500

sum_price = (coffe_price * 3) + (cake_price * 2)
print(sum_price)



# 과제 B. 학습 시간 변환
total_minutes = 385
hour = total_minutes / 60 # 6 예상.
minutes = total_minutes % 60 # 25 예상.
print(f"시간:{int(hour)} 분:{minutes}")



# 과제 C. 직사각형 계산
width = 12
height = 8

area = width * height # 96 예상
print("넓이",area) 
print(area > 100)
width += 3
new_area = width * height
print("+=3 적용 넓이",new_area)