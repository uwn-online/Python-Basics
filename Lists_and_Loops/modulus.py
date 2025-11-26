# Fizzbuzz
""" At the count of 40, if a number is divisble by 3, Fizz; if a number is divisible by 5, Buzz; 
if a number is divisible by 3 &5, fizzbuzz
"""

n = 100
for i in range(1, n+1): # calculates froom 1 to 101
    if i % 3 == 0 and i % 5 == 0:
        print(i, "Fizzbuzz!!")
    elif i % 5 == 0:
        print(i, "Buzz!")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)

""" Ask user to input a string and then print it out to the screen in reverse order"""

word = input("Please enter a word: ")
reverse_string = ''
for char in word:
    reverse_string = char + reverse_string
print(reverse_string)