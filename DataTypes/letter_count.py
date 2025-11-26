
reddit = """
So how can I build habits then? Do it based on willpower. The big difference is not to say to yourself 

"I'm gonna read 20 pages every day because I'm so motivated to gain knowledge." 

But that you say "I'm going force myself to start reading everyday because I will have enough willpower to always do that."

The key is that if you make the requirement so small that you can always do it, you will never fail.

So doing for example 1 pushup everyday. You will never fail that requirement. 

But if you have very little motivation one day and think about doing 20 pushups, 

it just seems intimidating and you don't do it.

Some people might say "only starting to read or doing 1 push up will never get me anywhere." 

And I agree, but the thing is that you can do more. And you will usually do more. 

Once you forced yourself, with willpower, to get into push up position and do 1 push up, you'll probably think 

"I can do one more, and one more" and so on. Same for reading, 

once you've forced yourself to sit in a chair with a book and started reading, you wont stop after just 1 word.

"""

letter_count = {}
for letter in reddit:
    letter_count[letter.lower()] = letter_count.get(letter, 0) + 1
print(letter_count)


from collections import Counter
print(Counter(reddit.lower()))

# Create a new dictionary from reddit variable
new_dict = dict(Counter(reddit.lower()))

print(new_dict)

print()

new_dict = {k:v for k, v in new_dict.items() if k.isalpha()} # this assigns key-value pairs if made up of letters(a-z)
print(new_dict)