text = "   Learning Python   is fun and   engaging! Let's    split these words properly.   "

# Use split() to separate text into individual words
words = text.split() #Assign variable to store the split

print(words)

# Tuples 
""" Unlike a lists and dictionaries, tuples like strings are immutable. They are used in Key elements in the dictionary"""

tuple_1 = (2, 4, 5, 6)
print(tuple_1[0:])

#Nested lists
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[0][2]) # This access the content of the list in index 2 of list index 0


# Creating a dictionary where the value pairs are dictionaries.

countries = {'France': {'Capital':'Paris', 'Language':'French'}, 'Spain': {'Capital':'Madrid', 'Language':'Espanola'},
             'United Kingdom': {'Capital':'London', 'Language':'English'}
             }

print(countries['France'])

for key, value in countries.items():
    print(key, value)

for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}')

# Books titles.
library = {
    "Fiction": [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"}
    ],
    "Science": [
        {"title": "A Brief History of Time", "author": "Stephen Hawking"},
        {"title": "The Selfish Gene", "author": "Richard Dawkins"}
    ],
    "History": [
        {"title": "Sapiens", "author": "Yuval Noah Harari"},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond"}
    ]
}

# Print the title of the first fiction book
print("First fiction book title:", library['Fiction'][0]['title'])

# Print the author of the second science book
print("Second Science book author:", library['Science'][1]['author'])

# What is the histor book's title and author
for book in library['History']:
    print(f"In the history category, we have {book['title']} by {book['author']}")

