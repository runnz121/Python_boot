def find_even_number(n,m):
    if n < m:
        numbers = [i for i in range(n, m+1)]
    else:
        numbers = [i for i in range(m, n+1)]
    mid = int((n + m+1)/2)


    print(f"첫 번째 수 입력 : {n}")
    print(f"두 번재 수 입력 : {m}")

    for i in numbers:
        if i == mid and i%2 == 0:
            print(f"{mid} 중앙값")
        elif i%2 ==0:
            print(f"{i} 짝수")
n = int(input("첫 번째 수 입력:"))
m = int(input("두 번째 수 입력:"))
print(find_even_number(n,m))