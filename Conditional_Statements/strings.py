my_string = 'Python'
print(len(my_string)) #Length of string
print(my_string[0:2]) #Slicing
print(my_string[-3:]) #character 


print(my_string.upper())
print(my_string.lower())




# Guessing game

word = 'summer'

guess = input("I'm thinking of a word, can you guess what it is? Hint: it's a season >> ").lower()


if guess == 'summer':
    print("Yes it's Summer. well done!")
elif guess == 'winter':
    print("No, it's not Winter, sorry!")
elif guess == 'autumn':
    print("No, it's not Autumn, sorry!")
elif guess == 'spring':
    print("No, it's not Spring, sorry!")
else:
    print(guess.capitalize(),'is not a season')






