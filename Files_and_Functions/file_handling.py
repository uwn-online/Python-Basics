
# File handling
# f = open('kipling.txt', 'w')

# f.write('Why is the weather so terrible and dull these days i think it has to do with climate change, \n')
# f.write('I see, and I do believe that you are on the right path \n')

# f.close()

# f = open('kipling.txt', 'r')
# print(f.read())
# f.close()

# f = open('kipling.txt', 'r')
# print(f.readlines()) #Creates a list
# f.close()

# To append content to a file
# f = open('kipling.txt', 'a')
# f.write('Thank you professor for believing in me.')
# f.close()

# f = open('kipling.txt', 'r')
# print(f.read())

with open('kipling.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')