# data = [53, 44, 45, 21, 33, 56, 67, 90]
# print(data[-4])

# for num in data:
#     print(num, end= ' ')

# total = 0
# for num in data:
#     total = total + num
# print('The sum total is', total)

# # Append 
# data.append(100) # Appends to the list
# data.extend([203, 301])
# print(data)


# # While loop
# """ While loops carries on looping as long as conditions are true """

# n = 10
# while n > 0:
#     print(n)
#     n = n-1

# user_input = int(input("Please input ages of class member:   ")) # Assign variable
# age = [] #An empty list for appending ages
# while user_input > 0:
#     age.append(user_input) # Input/append the user_input to the empty list
#     user_input = int(input("The next age of classmate:  "))
# print("The ages are", age)

# # Putting a counter in a while loop
# count = 0
# student_names = []
# user_name = input("Please enter student's names, type n at the final entry to close application:   ")
# while user_name != 'n':
#     count +=1 # Increases number of entries
#     student_names.append(user_name) #Append the entry into the empty list
#     print(f'{user_name} has been added!')
#     user_name = input('Input next name:  ')
# print(f'there are {count} students in the class, they are {student_names}')


participants = ['Ugo', 'Emeka', 'Ginka']
print(participants[1])

participants[2] = "Junior"

print(participants)

del participants[1]
print(participants)

participants.append('Juginho')
print(participants)

participants.extend(['Amen', 'Gunn'])
print('The first participant in our games is ' + participants[0] + '.')

"Alice, 35, france"
name, age, country = "Alice, 35, france".split()
print(name, age, country)


age = 27
print('Josh is ' ,age)