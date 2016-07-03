import itertools
tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    arr = map(int, input().split())

    count_even = 0
    count_odd = 0

    for i in arr:
        if i%2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print(count_even*count_odd)