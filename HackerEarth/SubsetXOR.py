from sys import getsizeof
tc = int(input())

while tc>0:
    tc -= 1

    n = int(input())
    arr = list(map(int, input().split()))

    ans = getsizeof(arr) / getsizeof(arr[0])

    if n == 1:
        print(arr[0])
    elif int(ans) == 1:
        print(arr[0])
    else:
        print(0)