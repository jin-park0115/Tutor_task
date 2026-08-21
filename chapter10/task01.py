# 과제 A - 카운트다운

# 사용자에게 시작 숫자를 입력 받는다.
start_num = int(input("숫자를 입력해주세요."))


for i in range(start_num, 0, -1):
    print(i)
print("시작!!")

## java랑 다른점 
# for(int i = start_num; i > 0; i--){
#   print(i) 
# }
# print("시작")

## 증감 연산자가 range에 넣는다... 헷갈린다.