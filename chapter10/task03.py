# 과제 C - 합계 계산기

number = int(input("숫자를 입력해주세요: "))

res = 0
for i in range(1, number+1):
    res += i
    print(f"{i} 번째 숫자")
print(res)