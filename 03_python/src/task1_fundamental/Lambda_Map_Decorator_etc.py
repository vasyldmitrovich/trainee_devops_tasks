print("Start seeing example")

# Initial list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the original list
print(f"Original list: {numbers}")

# Using list comprehension to create a new list with squares of each number
squares = [n ** 2 for n in numbers]
print("The loop iterates over each number in 'numbers' and computes its square.")
print(f"Squares of the numbers: {squares}")

# Using list comprehension to filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print("The loop iterates over 'numbers' and selects only the even numbers.")
print(f"Even numbers: {evens}")

# Using list comprehension to create a list of tuples (number, square)
number_square_pairs = [(n, n ** 2) for n in numbers]
print("The loop iterates over 'numbers' and creates tuples (number, square).")
print(f"Number-square pairs: {number_square_pairs}")

# Using list comprehension to create a new list for numbers greater than 5
greater_than_five = [n for n in numbers if n > 5]
print("The loop iterates over 'numbers' and selects numbers greater than 5.")
print(f"Numbers greater than 5: {greater_than_five}")
print("---")

# Informing that we're working with List Comprehensions
print("We are working with List Comprehensions and multi-variable functions using zip.")

# Lists of numbers
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# Printing the original lists
print(f"Original list1: {list1}")
print(f"Original list2: {list2}")

# Using zip to pair elements from list1 and list2
paired = list(zip(list1, list2))
print("The function 'zip' pairs elements from 'list1' and 'list2'.")
print(f"Paired elements: {paired}")

# Using list comprehension with zip to add elements from list1 and list2
summed = [x + y for x, y in zip(list1, list2)]
print("The loop iterates over the paired elements from 'list1' and 'list2' using 'zip', adding them together.")
print(f"Summed elements: {summed}")

# Using list comprehension with zip to multiply elements from list1 and list2
multiplied = [x * y for x, y in zip(list1, list2)]
print("The loop iterates over the paired elements from 'list1' and 'list2' using 'zip', multiplying them together.")
print(f"Multiplied elements: {multiplied}")

# Using list comprehension with zip to create formatted strings from list1 and list2
formatted = [f"{x} + {y} = {x + y}" for x, y in zip(list1, list2)]
print("The loop iterates over the paired elements and formats them into strings showing their addition.")
print(f"Formatted addition results: {formatted}")
print("---")

# Informing that we're working with lambda vs def
print("We are working with lambda vs def.")


# Using def to define a regular function for addition
def add_def(x, y):
    return x + y


# Using lambda to define a function for addition
add_lambda = lambda x, y: x + y

# Calling the functions and printing results
result_def = add_def(3, 5)
print(f"Using def: 3 + 5 = {result_def}")

result_lambda = add_lambda(3, 5)
print(f"Using lambda: 3 + 5 = {result_lambda}")

# Another example with more complex lambda function (calculating square)
square_def = lambda x: x ** 2
print(f"Using lambda to calculate square of 4: {square_def(4)}")


# Defining similar functionality using def
def square_def_func(x):
    return x ** 2


print(f"Using def to calculate square of 4: {square_def_func(4)}")

# Finishing with separator
print("---")

# Informing that we are working with lambda functions
print("We are working with an anonymous (lambda) function.")

# Defining a lambda function for addition
add = lambda x, y: x + y

# Printing the lambda function (it shows that it's a lambda object)
print(f"Lambda function: {add}")

# Using the lambda function
result = add(7, 3)
print(f"Using lambda to add 7 and 3: {result}")

# Another example: Lambda function to calculate the square of a number
square = lambda x: x ** 2

# Using the lambda function to calculate the square of 5
print(f"Using lambda to calculate the square of 5: {square(5)}")

# Example of lambda function with a list and filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Printing the result of filtering even numbers
print(f"Using lambda to filter even numbers from the list {numbers}: {even_numbers}")

# Another example: Lambda to multiply two numbers
multiply = lambda a, b: a * b

# Using the lambda function to multiply 4 by 5
print(f"Using lambda to multiply 4 and 5: {multiply(4, 5)}")

# Finishing with separator
print("---")

# Informing about map example
print("Example with map:")

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Output the result
print(f"Original list: {numbers}")
print(f"Squared list using map: {squared_numbers}")
print("---")

# Informing about filter example
print("Example with filter:")

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Using filter with a lambda function to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Output the result
print(f"Original list: {numbers}")
print(f"Filtered even numbers: {even_numbers}")
print("---")

# Informing about reduce example
print("Example with reduce:")

# Importing reduce from functools
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce with a lambda function to calculate the product of all numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# Output the result
print(f"Original list: {numbers}")
print(f"Product of all numbers using reduce: {product_of_numbers}")
print("---")

# Define a list
my_list = [10, 20, 30, 40]

# Get the iterator object using iter()
my_iterator = iter(my_list)

# Call next() to get the next value from the iterator
print("Calling next(my_iterator) the first time:", next(my_iterator))  # Output: 10
print("Calling next(my_iterator) the second time:", next(my_iterator))  # Output: 20
print("Calling next(my_iterator) the third time:", next(my_iterator))  # Output: 30
print("Calling next(my_iterator) the fourth time:", next(my_iterator))  # Output: 40

# If we call next() again, it will raise a StopIteration exception
try:
    print("Calling next(my_iterator) again:", next(my_iterator))  # This will raise StopIteration
except StopIteration:
    print("No more elements to iterate over!")


# Custom iterable class that returns numbers from 1 to 5
class MyIterable:
    def __init__(self):
        # Initialize the list and the index for iteration
        self.numbers = [1, 2, 3, 4, 5]
        self.index = 0

    def __iter__(self):
        # The __iter__ method returns the iterator object (in this case, the object itself)
        return self

    def __next__(self):
        # The __next__ method is called to get the next value in the sequence
        if self.index < len(self.numbers):
            number = self.numbers[self.index]
            self.index += 1
            return number
        else:
            # If there are no more elements, raise StopIteration
            raise StopIteration


# Create an instance of MyIterable
my_iterable = MyIterable()

# Iterate through the custom iterable using a for loop
print("Iterating through MyIterable:")
for num in my_iterable:
    print(num)
print("---")


# Define a simple generator function
def my_generator():
    # This function will yield values one by one
    for i in range(1, 6):
        print(f"Yielding {i}")
        yield i  # Yield the current value of 'i'


# Create a generator object
gen = my_generator()

# Iterate over the generator object
print("Iterating through the generator:")
for value in gen:
    print(f"Received {value}")

# Generator expression example
gen_expr = (x ** 2 for x in range(1, 6))

print("Iterating through generator expression:")
for value in gen_expr:
    print(f"Square: {value}")


# Infinite generator of even numbers
def even_numbers():
    n = 0
    while True:
        yield n  # Yield the next even number
        n += 2


# Create the generator
evens = even_numbers()

# Get the first 5 even numbers using next()
print("Fetching the first 5 even numbers:")
for _ in range(5):
    print(next(evens))  # Manually call next to get values

print("---")


# Defining a basic generator function
def number_generator():
    print("Generator started")
    for i in range(1, 6):
        print(f"Yielding value: {i}")
        yield i  # Yielding the value, pauses the function until next is called


# Creating a generator object
gen = number_generator()

# Iterating over the generator object
print("Iterating through the generator:")
for value in gen:
    print(f"Received: {value}")
print("---")  # Separator for console output


# Basic decorator that prints before and after calling the original function
def simple_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


# Applying the decorator using @ syntax
@simple_decorator
def say_hello():
    print("Hello!")


# Calling the decorated function
print("Calling decorated function:")
say_hello()
print("---")


# First decorator
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()

    return wrapper


# Second decorator
def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()

    return wrapper


# Applying both decorators
@decorator_one
@decorator_two
def say_goodbye():
    print("Goodbye!")


# Calling the function decorated by both decorators
print("Calling function with chained decorators:")
say_goodbye()
print("---")


# Decorator that prints the arguments passed to the function
def print_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


# Function that takes two parameters
@print_arguments
def add(a, b):
    return a + b


# Calling the decorated function with arguments
print("Calling decorated function with arguments:")
result = add(3, 4)
print(f"Result of add(3, 4): {result}")
print("---")


# First decorator that multiplies result by 2
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


# Second decorator that subtracts 1 from the result
def subtract_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result - 1

    return wrapper


# Applying both decorators to a function with parameters
@double_result
@subtract_one
def multiply(a, b):
    return a * b


# Calling the decorated function
print("Calling function with chained decorators and parameters:")
result = multiply(5, 4)
print(f"Result of multiply(5, 4): {result}")
print("---")
