#variables are passed through functions

def hello():
    print("Hello World!")

hello()

def user_name(name):
    print(f'Hello, {name}')

user_name('ugo')

# Key word argument
def user_name_2(name = 'input name, please!'):
    print(f'Hello, {name}')

user_name_2()

# Fibonacci sequence in a function
def fib(n):
    """Calculates and returns the nth fibonacci number"""
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a
fib_num = fib(20)
print(fib_num)

for i in range(20):
    print(fib(i))


# Function to calculate average of numbers

def calc_mean(first, *remainder):
    """This calculates the mean of numbers"""
    mean = (first + sum(remainder))/(1+len(remainder)) 
    return mean


print(calc_mean(23,344, 34, 1, 22, 65, 76, 344, 677, 555))



# Step 1: Define the calculate_mean function
def calculate_mean(first, *remainder):
  if first is None and not remainder:
    print('No values provided')
    return
  mean = (first + sum(remainder))/(1+len(remainder))
  return mean
  
# Step 2: Test the function
mean = calculate_mean(10, 20, 30)
print("The mean of 10, 20, 30 is:", mean)

mean = calculate_mean(5, 15, 25, 35, 45)
print("The mean of 5, 15, 25, 35, 45 is:",mean)


def plus_ten(a):
    result = a +10
    return result
print(plus_ten(15))

def multiplication_by_7(x):
    result = x * 7
    print(x, 'multiplied by 7 equals', result)
    return result

print(multiplication_by_7(5))

"""To use function within a function"""
def wage(w_hours):
    return w_hours * 25

def with_bonus(w_hours):
    return wage(w_hours) + 50

print(wage(10), with_bonus(10))

# Subtract, divide, and rule the numbers!
def minus_ten(x):
    """This function subtracts 10 from its argument"""
    return x - 10
def d_by_5(x):
    """Thiss function first subtracts 10, then divide the result by 5"""
    return minus_ten(x)/5

print(d_by_5(200))

"""Combining Conditional statements and Functions togther."""
def add_ten(a):
    """This function adds ten if a = 100 or more."""
    if a >= 100:
        a = a + 10
        return a
    else:
        return "Save more, John!"
    
print(add_ten(120))
print(add_ten(30))

def compare_and_subtract(x,y):
    if x > y:
        print("The difference between the two values is", (x-y))
    elif x < y:
        print("The sum of the two values is", (x+y))
    else:
        print("The two values are equal")
    return "" # This prevent unintended none appearing as output.

print(compare_and_subtract(13, 5))

"""Working with more than one parameter in a function."""

def multiple_parameter(a,b,c):
    result = a - b*c
    print('Parameter a equals', a)
    print('Parameter b equals', b)
    print('Parameter c equals', c)
    return result

c = multiple_parameter(20, 10, 5)
print(c)