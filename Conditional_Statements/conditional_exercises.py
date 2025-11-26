# Exercise one.
# Write a code that asks for input between 1 and 5, the code will take the integer value and print out the string value. 

user_input = int(input('please input a selection between 1 and 5 >> '))

if user_input == 1:
    print("One")
elif user_input == 2:
    print("Two")
elif user_input == 3:
    print("Three")
elif user_input == 4:
    print("Four")
elif user_input == 5:
    print("Five")
else:
    print("selection out of range, Try again between 1 and 5")


# Exercise two.
""" Repeat the previous task but this time the user will input a string and the 
code will ouput the integer value. Convert the string to lowercase first. """

user_input_2 = str(input('Please input selection between one and five in words, please!>>  ')).lower()

if user_input_2 == 'one':
    print(1)
elif user_input_2 == 'two':
    print(2)
elif user_input_2 == 'three':
    print(3)
elif user_input_2 == 'four':
    print(4)
elif user_input_2 == 'five':
    print(5)
else:
    print('Out of range, try again!')


# Exercise three.
# Create a variable containing an integer between 1 and 10, ask user to guess and if too low, they lost, if too high they won.

secret_number = 5

guess_number = int(input('Please enter a selection between 1 and 10 >>  '))

if guess_number == secret_number:
    print("You guessed the correct number!")
elif guess_number > secret_number and guess_number <=10:
    print("Number too high, try again")
elif guess_number < secret_number and guess_number >=1:
    print("Entry too low, try again")
else:
    print("Out of range")


# Exercise Four.
# Naming characters.
name = input("Please input your names here:  ")
name_len = len(name)

if name_len > 5:
    print('Your name contains' ,name_len, 'characters.')
else:
    print("The length of your name is a secret!.")


# Exercise five.
''' Ask the user for two integers between 1 and 20. If they are both greater than 
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero '''

user_selection_1 = int(input("Please input integers between 1 and 20:  "))
user_selection_2 = int(input("Please input integers between 1 and 20 for selection 2:  "))



if user_selection_1 > 15 and user_selection_2 > 15:
    print(user_selection_1 * user_selection_2)
elif user_selection_1 > 15 or user_selection_2 > 15:
    print(user_selection_1 + user_selection_2)
else:
    print(0)


# Exercise six.

"""  Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
 """

var_1 = int(input("Please enter first integer:  "))
var_2 = int(input("Please enter second integer:  "))
swap =  var_1, var_2 = var_2, var_1
print(swap)