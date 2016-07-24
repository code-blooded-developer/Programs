from math import sqrt
tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    count = 0

    a = 2
    b = n-(a+2)
    while a<b:
        while a<b:
            a_sq = a*a
            b_sq = b*b

            c_sq = a_sq + b_sq
            c = sqrt(c_sq)

            if c < b:
                continue
            if a+b+c == n:
                count = count + 1
            b = b - 1
        a = a + 1
        b = n-a+2

    print count