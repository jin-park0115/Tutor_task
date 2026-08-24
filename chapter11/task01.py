scores = []

for i in range(0,5):
    scores.append(int(input("점수를 입력해주세여: ")))

total = 0
min_score = min(scores)
max_score = max(scores)

for score in scores:
    total += score
print(f"총점: {total}")

print(f"최저점: {min_score}")
print(f"최고점: {max_score}")

avg = total / len(scores)
print(f"평균: {avg}")

for i in scores:
    if(i >= 80):
        print(i)
scores.sort()
print(scores)