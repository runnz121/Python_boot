import random

def solution():
    computer = random.randint(0,2)
    my = input("가위 바위 보!:") #my = input("0 1 2:")
    if my == '가위' or 0:
        if computer == 0:
            print("나:" + my)
            print("컴퓨터: 가위")
            print("비김")
        elif computer == 1:
            print("나:" + my)
            print("컴퓨터: 바위")
            print("컴퓨터 승리!!")
        elif computer == 2:
            print("나:" + my)
            print("컴퓨터: 보")
            print("승리")
    elif my == '바위' or 1:
        if computer == 0:
            print("나:" + my)
            print("컴퓨터: 가위")
            print("승리!!")
        elif computer == 1:
            print("나:" + my)
            print("컴퓨터: 바위")
            print("비김")
        elif computer == 2:
            print("나:" + my)
            print("컴퓨터: 보")
            print("컴퓨터 승리!!")
    elif my == '보' or 2:
        if computer == 0:
            print("나:" + my)
            print("컴퓨터: 가위")
            print("컴퓨터 승리!!")
        elif computer == 1:
            print("나:" + my)
            print("컴퓨터: 바위")
            print("승리!!")
        elif computer == 2:
            print("나:" + my)
            print("컴퓨터: 보")
            print("비김")
    return


print(solution())
