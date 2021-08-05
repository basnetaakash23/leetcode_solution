def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    first = 0
    second = 1

    for x in range(2,n+1):
        s = first + second
        first = second
        second = s

    return s

print(fibonacci(1000))