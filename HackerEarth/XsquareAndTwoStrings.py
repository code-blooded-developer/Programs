tc = int(input())

while tc > 0:
    tc -= 1

    s1 = input()
    s2 = input()

    present = False;

    for char in s1:
        if char in s2:
            present = True
            break

    if present:
        print('Yes')
    else:
        print('No')
