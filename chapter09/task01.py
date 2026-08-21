# 과제 A - 연령 안내 프로그램
age = int(input("나이를 입력해주세요: "))

if(age < 8 ):
    print("미취학 입니다.")
elif(age < 14):
    print("초등학생 입니다.")
elif(age<17):
    print("중학생 입니다.")
elif(age<20):
    print("고등학생 입니다.")
else:
    print("성인 입니다.")