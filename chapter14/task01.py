# 학생 점수 보고서 함수 만들기

name = "민수"
scores = [85,90,95]


def calculate_average(scores):  
    return sum(scores) // len(scores)


def get_grade(score):
    if(score >= 90):
        return "A"
    elif(score >=80):
        return "B"
    else:
        return "C"
    



def show_report(name, average, grade):

    return f"{name}, 평균: {average}, 등급:{grade}"

avg_score = calculate_average(scores)
grade = get_grade(avg_score)
print(show_report(name, avg_score, grade))