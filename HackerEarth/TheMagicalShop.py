a,b = map(int, raw_input().split())

string = raw_input()

ans = 0

for i in string:
    if i == '1':
        ans = int((ans + a)%b)

    a = int((a*a)%b)

print(ans)