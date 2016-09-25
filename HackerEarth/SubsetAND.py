import itertools

def findsubsets(S,m):
    return list(itertools.combinations(S, m))

def andSet(set):
    result = set[0]
    i = 1
    while i < len(set):
        result = result & set[i]
        i += 1

    return result

tc = int(input())

while tc > 0:
    tc -=1

    z, n = map(int, input().split())

    s = list(map(int, input().split()))

    exist = False

    for i in range(n):
        if exist:
            break
        subset = findsubsets(s, i+1)

        for set in subset:
            if z & andSet(list(set)) == 0:
                exist = True
                break

    if exist:
        print('Yes')
    else:
        print('No')


