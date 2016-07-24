tc = int(input())

while tc > 0:
    tc -= 1
    n = int(input())

    ans  = 0

    for i in range(1,n+1):
        j = i+1
        while j <= n:
            if i^j <= n:
                ans += 1
            j += 1

    print(ans)