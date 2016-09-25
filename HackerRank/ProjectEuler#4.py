tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    flag = False

    for i in reversed(range(10000,998002)):
        str1 = str(i)
        str2 = str(i)[::-1]

        if str1 == str2 and i < n:

            for j in range(100, 1000):
                if i%j == 0 and i/j <= 999:
                    print(i)
                    flag = True
                    break

        if flag:
            break