# 과제 01.
# 과제 목표
# 실제 정보를 어떤 변수 이름과 데이터형으로 표현할지 스스로 결정합니다.

product_name = "iPhone17 Pro Max"
price = 1800000
discount_rate = 0
is_on_sale = True
stock = 28


# 과제 02. 데이터 형 예상

# product_name == str
# price == int
# discount_rate == int
# is_on_sale == bool
# stock == int

# 과제 03. type()으로 검증
print(type(product_name)) #<class 'str'>
print(type(price)) #<class 'int'>
print(type(discount_rate)) #<class 'int'>
print(type(is_on_sale)) #<class 'bool'>
print(type(stock)) #<class 'int'>

# 과제 04. 형 변환
# price 문자열로 바꾸기
price_str = str(price)
print(type(price_str))

# 과제 05. 오류 실험
# int("파이썬")
# 파이썬은 int로 형 변환이 되지 않는다.