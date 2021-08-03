def gugudan(number):
    i = 0
    print(f"{number} 단")
    while i < 50:
        if i%2 != 0:
            res = number * i
            print(f"{number} X {i} = {res}")
        i = i+1
    return
number = int(input("몇 단?:"))
print(gugudan(number))