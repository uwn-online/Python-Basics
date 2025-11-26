"""Write a code to calculate the first 20 fibonacci numbers"""

# Number of fibonacci numbers required
n = 20

# set a and b to the first two numbers in the sequence
a = 0
b = 1

# List in which to store numbers
fib_nums = []

# Use a foor loop to create the sequence, repeat n times
for i in range(n):
    fib_nums.append(a)
    a,b = b, a+b 
print(f'The first {n} fibonacci numbers are , {fib_nums}')

""" Write a cod that will determine all odd and even numbers between 1 and 100. Put the odds in a list named odd and
the evens in a list named even"""

#Numbers required 
n = 100

# Create lists to contain odd and even numbers
evens = []
odds = []

for x in range(n+1):
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
print(f'The even numbers are {evens}')
print(f'The odd numbers are {odds}')