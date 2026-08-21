# 과제 C - 여행 경비 계산기

travel = input("여행지를 입력해주세요: ")
estimated_cost = int(input("1일 예상 비용을 입력해주세요: "))
travel_days = int(input("여행 일수를 입력해주세요: "))

total_cost = estimated_cost * travel_days
print(f"여행지: {travel}, 전체 예상 비용: {total_cost}")