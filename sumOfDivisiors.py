def sumOfDivisors(N):
    k = 0
    for i in range(1, N+1):
        k += i * (N // i)
    print(k)

sumOfDivisors(5)