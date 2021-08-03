def bus_fare(age,type):
    cash = 0

    if(age < 8):
        cash = 0
    elif(8 <= age < 14 ):
        cash = 450
    elif(14 <= age <20):
        if(type =='카드'):
            cash = 720
        else:
            cash = 1000
    elif(20 <= age < 75):
        if(type =='카드'):
            cash = 1200
        else:
            cash = 1300
    elif(age>=75):
        cash = 0

    if(cash == 0):
        cash = '무료'

    print("나이:" + str(age) + "tp")
    print("지불유형:" + str(type))
    print("버스요금:" + str(cash) + "원")
bus_fare(30,"현금")