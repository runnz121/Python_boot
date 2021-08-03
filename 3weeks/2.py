import random

def rsp_advanced(games):
    i = 0
    winme = 0
    wincom = 0
    draw = 0
    while(i < games):
        game = input("가위, 바위 보 중 하나를 내세요 : \n")
        if game != "0" and game != "1" and game != "2" and game != "가위" and game != "바위" and game != "보":
            game = input("다시 입력해주세요 : \n")
        # 0 < 1 < 2
        # 가위 < 바위 <보
        if game == "가위" or game == "1":
            game = 1
        elif game == "바위" or game == "2":
            game = 2
        elif game == "보" or game == "3":
            game = 3

        computer = random.randint(0, 2)

        if computer < game:
            res = "나의 승리"
            winme +=1
        elif computer == game:
            res = "무승부"
            draw +=1
        else:
            res = "컴퓨터의 승리"
            wincom +=1

        if game == 1 and computer == 1:
            game = "가위"
            computer = "가위"
        elif game == 2 and computer == 2:
            game = "바위"
            computer = "바위"
        elif game == 3 and computer == 3:
            game = "보"
            computer = "보"

        print(f"가위 바위 보 : {i}")
        print(f"나 : {game}")
        print(f"컴퓨터 : {computer}")
        print(f"{i+1} 번째 판 {res}\n")
        i += 1

    print(f"나의 전적 : {winme}승 {draw}무 {wincom}패")
    print(f"컴퓨터의 전적 : {wincom}승 {draw}무 {winme}패")

games = int(input("몇 판을 진행하시겠습니까? : "))
print(rsp_advanced(games))