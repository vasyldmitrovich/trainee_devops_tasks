#

print("Start working with functions")


def first(par1):
    print(f"First function running, parameter passed in this function is: {par1}")


print(f"first('Hello'): {first('Hello')}")


def with_return(par1, par2):
    '''This function get par1 and par2 and add those parameters'''
    return par1 + par2


print(f"with_return(2, 5): {with_return(2, 5)}. \t\tPrint doc: {with_return.__doc__}")


def my_fun_with_default_param1(p1, p2=10):
    return p1 + p2


print(f"my_fun_with_default_param1(87) With dufault p2=10: {my_fun_with_default_param1(87)}")
print("---")


def fun1(p1, p2='5'):
    return "From function, p1: " + p1 + ", p2: " + p2


print("Function is: \t\t\tdef fun1(p1, p2='5')")
print(f"fun1(p2='4', p1='7string'): {fun1(p2='4', p1='7string')}")
print(f"fun1(444): {fun1('444')}")
print("---")


def arbitrary_fun(*name):
    for i in name:
        print(f"Val: {i}")


print("Function is: \t\t\tdef arbitrary_fun(*name)")
print(
    f"arbitrary_fun('One', 'Tso', 'Third par', 'Forth_par') : {arbitrary_fun('One', 'Tso', 'Third par', 'Forth_par')}")
print("---")


def print_numbers(number, *args):
    print("argument: ")
    print(number)
    print("vartuple: ")
    for var in args:
        print(var)


print("Function is: \t\t\tdef print_numbers(number, *args)")
print(f"print_numbers(1,3,88,56): {print_numbers(1, 3, 88, 56)}")
print("---")


def scope_func():
    x = 10
    print("Value inside function:", x)


x = 20
scope_func()
print("Value outside function:", x)
print("---")

globalVar = 'variable value'


def someFun():
    gV1 = globalVar + '_hello'
    print("Get data from global var and set to local variable gV1: ", gV1)


someFun()
print("globalVar: ", globalVar)
print(f"Change global var from function")


def someFun1():
    global globalVar
    globalVar = globalVar * 3


someFun1()
print("globalVar: ", globalVar)
print("---")


def outer_function():
    outer_var = "I am outside!"

    def inner_function():
        nonlocal outer_var  # Use nonlocal, for changing variable from outside function
        outer_var = "I am modified inside!"
        inner_var = "I am inside!"  # Local variable inside inner_function
        print(inner_var)

    inner_function()
    print(outer_var)  # After calling inner_function variable outer_var will be changed


outer_function()
print("---")


def recursive_function(counter):
    # Base case: Stop recursion when counter reaches 4
    if counter == 4:
        print("Reached 4, stopping recursion.")
        return

    # Print the current iteration
    print(f"Recursion iteration: {counter}")

    # Recursive call, increment the counter
    recursive_function(counter + 1)


# Initial call to the recursive function with starting counter at 0
recursive_function(0)
print("---")

# Lambda function that adds two numbers
add = lambda x, y: x + y

# Example usage
result = add(3, 5)
print(f"lambda x, y: x + y \tResult: ", result)  # Output: 8

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Lambda function to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert the result to a set
squared_set = set(squared_numbers)

# Output the set
print(squared_set)  # Example output: {1, 4, 9, 16, 25}
