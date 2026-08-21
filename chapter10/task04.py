password = "123455"


# while True:
#     password_in= input("비밀번호를 입력하세요: ")
#     if(password == password_in):
#         print("로그인 성공!")
#         break
#     print("다시 입력하세요")

count = 0
maxtry = 5

while count < maxtry:
    password_in= input("비밀번호를 입력하세요: ")
    if(password == password_in):
        print("로그인 성공!")
        break
    count += 1
    print("다시 입력하세요")
print("5회 틀리셨으므로 종료 됩니다.")