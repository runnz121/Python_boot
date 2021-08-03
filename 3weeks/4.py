
def count_prime_number(n,m):
    if n < m:
        numbers = [i for i in range(n, m+1)]
    else:
        numbers = [i for i in range(m, n+1)]
    nl = len(numbers)
    is_prime = [True] * nl

    max_len = int(nl**0.5)
    for i in range(2, max_len+1):
        if is_prime[i] == True:
            for j in range(i+i, nl, i):
                is_prime[j] = False

    primes = [i for i in range(2, nl) if is_prime[i] == True]

    print(primes)
    print(f"소수개수 {len(primes)}")

n = int(input("첫 번쨰 수 입력 :"))
m = int(input("두 번째 수 입력 :"))
print(count_prime_number(n,m))