from math import sqrt

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


n = int(input())

sieve = primes(10005)

for i in range(0,n):
    beer = int(input())

    sq = sqrt(beer)

    if beer == 1:
        print('NO')
    elif beer in sieve:
        print('NO')
    elif sq*sq == beer and sq in sieve:
        print('NO')
    else:
        print('YES')


