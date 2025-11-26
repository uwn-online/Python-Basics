""" Countdown timer exercise"""

n = 10
while n>= 0:
    print(n)
    n -= 1 #decreases value of n by 1
print('Takeoff!')

# Sum of odd numbers using while loop
n = 1
odd_sum = 0
while n <= 20:
    if n % 2 != 0: #checks if the number is odd
        odd_sum += n #Adds one to odd_sum if the n is not odd
    n += 1 #increase n  by 1 for each iteration until it gets to 20
print("The sum of all odd numbers between 1 and 20 is:", odd_sum)