some_condition = True
if some_condition:
    print('The variable \'some_condition\' is True')
else:
    print('The variable \'some_condition\' is False')

# What should I wear?
temp = int(input('Please enter the temperature in celsius, must be an integer between 0-40 >>> ')) #Creating temperature variable

if temp > 30:
    print('Wear shorts and sun cream!')
elif temp <= 30 and temp > 20:
    print('It\'s warm out there, but not too sure shorts is a good choice!')
elif temp <= 20 and temp > 10:
    print('You \'ll need a cardigan')
else:
    print('Stay indoors, it\'s freezing!!')
    
weather = 'Rainy' #Assigned variable
if weather == 'Rainy':
    print("it's raining, take an umbrella")
elif weather == 'Sunny':
    print("It's sunny, wear sunglasses")
elif weather == 'Snowy':
    print("It's snowy, wear a warm coat!")
else:
    print("Weather is unpredictable")



# Driving permission program
age = int(input("Please input applicants age, must be an integer between 0 and 100 >>>"))
has_permission = str(input("Permission status: "))

if age >= 18 and has_permission == "yes":
    print("Can drive")
elif age <= 18 and has_permission == "yes":
    print("Can drive with permission")
elif age >= 18 and has_permission == "no":
    print("Cannot drive")
elif age > 100:
    print("Cannot drive")
else:
    print("Not permitted to drive!")


