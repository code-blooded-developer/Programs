tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    sum = 0

    p = 0
    x = 2
    flag = True
    while flag:
        if x > n:
            flag = False
        temp = x + int(2 << p)
        print(temp)
        if temp <= n:
            sum = int((sum+temp)%1000000007)
        else:
            flag = False
        p += 1
        x = 2 << p

    print(sum%1000000007)
