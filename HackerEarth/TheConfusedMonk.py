from fractions import gcd

n = int(input())

arr = list(map(int, raw_input().split()))

fx = 1
for i in arr:
    fx = fx * i

gx = reduce(gcd,arr)
quotient = 1000000007
ans = 1

while gx != 0:
    if gx%2 == 1:
        ans *= fx
        ans %= quotient

    fx *= fx
    fx %= quotient
    gx /= 2

    gx = int(gx)

print(ans)



