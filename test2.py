def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

tc = int(input())

while tc > 0:
    tc -= 1

    n = int(input())

    primes = primes(n+1)

    sum = 0

    for prime in primes:
        sum = sum + prime

    print(sum)