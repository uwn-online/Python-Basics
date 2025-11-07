def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
a = is_prime(313)
print(a)


count = 0
primes = []

for i in range(100, 151):
    if is_prime(i):
        count += 1
        primes.append(i)
print("Prime numbers:" ,primes)
print("Total Count:" ,count)