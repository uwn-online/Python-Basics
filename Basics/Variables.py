#Creating variables.

a = 2.5
b = 3.14159
print(b*a**2)

radius = 2.5
pi = 3.14
area = radius**2 * pi
print(area)

x= 10
y = 3
z = x * y
print(z)

len = 12
width = 5
perimeter = 2 * (len + width)
print(perimeter)


phrase_1 = 'The cat sat on the mat,'
phrase_2 = 'and so did the dog.'
phrase_3 = phrase_1 + ' '+ phrase_2 #Concatenates strings and adds space

print(phrase_3)

user_input = int(input('How many apples do you have? \n >>> ')) #input function for better interactivity
type(user_input) #Checks data type


repeat_phrase = 'Goodbye ' * 3
print(repeat_phrase)