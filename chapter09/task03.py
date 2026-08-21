# 과제 C - 간단한 로그인 판정
saved_id = "python"
saved_password = "123456"

id = input("아이디를 적어주세요: ")
password = input("비밀번호를 입력해주세요: ")

# if(saved_id != id):
#     print("id가 맞지 않습니다.")
# elif(saved_password != password):
#     print("비밀번호가 맞지 않습니다.")
# else:
#     print("로그인 되었습니다.")


print("로그인 되었습니다." if saved_id == id and saved_password == password else "id가 맞지 않습니다." if saved_id != id else "비밀번호가 맞지 않습니다.")