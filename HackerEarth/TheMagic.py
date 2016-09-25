tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    ans = bin(n).count("1")

    print(ans)
