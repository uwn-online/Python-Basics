from collections import Counter

# Text provided for analysis

text = """In data science, we often use machine learning models to predict outcomes based on input data.\n
Machine learning can be classified into three main types: supervised, unsupervised, and reinforcement learning.\n
Supervised learning involves training a model on labeled data, where the correct answer is already known.\n
In contrast, unsupervised learning finds patterns or structures within data without any labeled output.\n
Reinforcement learning is based on rewarding a model for making correct decisions and penalizing it for mistakes.\n
By understanding these types, we can choose the right model for our data and improve our predictions."""


# Count all characters using Counter on lowercase text
print(Counter(text.lower()))

print()

# Convert counter to dictionary
new_dict = dict(Counter(text.lower()))
print(new_dict)

print()

# Filter only alphabetic elements
new_dict = {k:v for k, v in new_dict.items() if k.isalpha()}
print(new_dict)