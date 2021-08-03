def grader(name,score):
    grade = ''
    if(100 >= score >= 95):
        grade = 'A+'
    elif(94 >= score > 90):
        grade = 'A'
    elif(89 >= score > 85):
        grade = 'B+'
    elif(84 >= score > 80):
        grade = 'B'
    elif(79 >= score > 75):
        grade = 'C+'
    elif (74 >= score > 70):
        grade = 'C'
    elif (69 >= score > 65):
        grade = 'D+'
    elif (64 >= score > 60):
        grade = 'D'
    elif (60 > score):
        grade = 'F'

    print("학생이름:" + str(name))
    print("점수:" + str(score))
    print("학점:" + str(grade))


print(grader("이호창",99))