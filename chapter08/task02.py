# 과제 B - 운동 시간 계산기

import re


def extract_integer(value):
	number = re.search(r"\d+", value)
	if number is None:
		raise ValueError("숫자가 포함된 값을 입력해주세요.")
	return int(number.group())


name = input("이름을 입력해주세요: ")
exercise_time = extract_integer(input("하루 운동 시간을 입력해주세요: "))
exercise_days = extract_integer(input("운동 일수를 입력해주세요: "))

total_exercise_time = exercise_time * exercise_days

print(f"{name}님의 총 운동시간은: {total_exercise_time}시간 입니다.")