# 과제 1. 데이터 준비

name = " 길동 "
email = "gildong@example.com"
city = "ilsan"
message = "I like Java"

# 과제 2. 문자열 정리

# 이름의 앞 뒤 공백 제거
strip_name = name.strip()
print(strip_name)

# 도시를 대문자로 변환
upper_message = message.upper()
print(upper_message)

# Java를 Python으로 교체
replace_message = message.replace("Java", "Python")
print(replace_message)

# 이메일 첫 글자와 마지막 글자 출력
print("이메일 첫글자:",email[0], "이메일 마지막 글자:",email[-1])

# 이메일 전체 길이 출력
print("이메일 전체 길이:", len(email))

# 과제 3. 인덱싱과 슬라이싱
# 이메일 앞 3글자를 출력합니다.
print("이메일 앞 3글자:",email[0:3])

# 이름의 첫 글자와 마지막 글자를 출력합니다.
print("이름의 첫 글자:",strip_name[0], "| 이름의 마지막 글자" ,strip_name[-1])

#자신이 선택한 문자열 한 개에서 원하는 범위를 슬라이싱 합니다.
print(replace_message[7:13])
print(replace_message[7:len(replace_message)])

# 과제 4.f-string출력
print(f"{strip_name}은 {city.upper()}에 살고 이메일은 {email} 입니다.")

# 과제 5. 오류 기록
# print("길동) syntaxError 수정 방법: 따옴표를 추가한다.
# print(strip_name[10]) index가 범위를 벗어났다고 오류가 난다. 최소 수정 방법 len을 확인 후 인덱스 범위를 수정한다.
# print(email + 10)  int가 아니라는 에러가 난다. 수정 방법: 숫자인 문자열은 int로 형 변환 하고, 문자인 문자열은 정수랑 더하지 않는다