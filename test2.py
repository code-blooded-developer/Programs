tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    count = 0

    while n:
        n = n & (n-1)
        count += 1

    print(count)