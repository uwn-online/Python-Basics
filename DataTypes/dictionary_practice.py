"""Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
"""
capitals = {'France':'Paris', 'Spain':'Madrid', 'United Kingdom':'London', 
            'India':'New Delhi', 'United States':'Washington DC', 'Italy':'Rome'
            ,'Denmark':'Copenhagen', 'Germany':'Berlin', 'Greece':'Athens'
            }

user_input = input("Please enter the country of interest: ").lower() #Converts input to lower

while ('united kingdom' not in user_input and not user_input.isalpha()): #Repeats the question until the user gives a proper country name (letters only) or types "united kingdom"

    if user_input == 'united states':
        break
    print('You must input a string')
    user_input = input('Which country would you like to check: ')
user_input = user_input.title()
print(user_input)
if user_input in capitals:
    print(f'The capital of {user_input} is {capitals[user_input]}')
else:
    print('No data available')


""" write python code that creates dictionary containing key value pairs for first 12 values of
fibonacci sequence """
n = 12
a = 0
b = 1
d = dict()
for i in range(1, n+1):
    d[i]= a
    a,b = b, a+b
print(d)

""" Days until christmas"""

import datetime
today = datetime.date.today()
print(f"Today's date is {today}")
holiday = datetime.date(2025, 12, 25)
delta = holiday - today
print(f"Just {delta.days} days until the holidays")


"""Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
"""

import random

keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = dict()

for letter in keys:
    d[letter] = random.randint(1,100) #Assigns key to the letters
print(d)

import matplotlib.pyplot as plt
x,y = zip(*d.items())
plt.bar(x,y)


""""Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
"""

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

deck = dict()
for i in suits:
    deck[i] = rank
print(deck)

# Calculating shirt sales at Challenger LTD.

shirt_sizes = [ 'M', 'XL', 'S', 'XS', 'L', '3XL', '2XL', '4XL',
               'XS', 'L', '3XL', '2XL', '4XL', 'M', 'XL', 'S', 'XS', 'L',
               'XL', 'S', 'XS', '4XL', 'M', 'XL','3XL', '2XL', 'L' ]

shirt_count = {} # Creats an empty dictionary to append output

for size in shirt_sizes:
    shirt_count[size] = shirt_count.get(size, 0) +1 #Adds count of sizes in the dictionary
print(shirt_count)


