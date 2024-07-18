import io
import sys

print("Hello World")

# In separate lines
print("Hello " \
      "my friend")
"""
Print in separate lines
"""
print("We work with \nPython")  # Add new line

variable1 = "Hello"
count = 3
print(f"Var variable1: {variable1}, count var is: {count}.")

var2 = 10
print(f"var2: {var2}, count: {count}")

print("count + var2 = ", count + var2)
print("count - var2 = ", count - var2)
print("count * var2 = ", count * var2)
print("count / var2 = ", count / var2)
print("count % var2 = ", count % var2)
print("Floor division count // var2 = ", count // var2)
print("Exponent count ** var2 = ", count ** var2)
print("-----")

number1 = 3 + 4 * 5 ** 2 + 7
print("3 + 4 * 5 ** 2 + 7 = ", number1)
number2 = (3 + 4) * (5 ** 2 + 7)
print("(3 + 4) * (5 ** 2 + 7) = ", number2)
number3 = 2 ** 3 ** 2
print("2**3**2 = ", number3)
number4 = (2 ** 3) ** 2
print("(2**3)**2 = ", number4)
print('---', 'end block with sep= * , end=!!! two new line, and flush=True', '---', sep=" * ", end='!!!\n\n', flush=True)  # forcibly flush the stream.

print("Working with err")
# Save the current stderr
original_stderr = sys.stderr
print("Save the current stderr    original_stderr = sys.stderr")

# Create a temporary stream for errors
temp_stderr = io.StringIO()
print("Create a temporary stream for errors    temp_stderr = io.StringIO()")

# Redirect stderr to the temporary stream
sys.stderr = temp_stderr
print("Redirect stderr to the temporary stream    sys.stderr = temp_stderr")

print('---This message passed to sys.stderr---', sep=" * ", file=sys.stderr)

# Get the content of the temporary stream
error_message = temp_stderr.getvalue()
print("Get the content of the temporary stream    error_message = temp_stderr.getvalue()")

# Restore the original stderr
sys.stderr = original_stderr
print("Restore the original stderr    sys.stderr = original_stderr")

# Print the error message to stdout
print("Captured error message: ", error_message)

print('-', 'New block', '-', sep=" ")

#number = int(input("Input integer number: "))
number = int(6)
print("Int variable number = int(6) is:", number, type(number))
#num = input("by default input number is string: ")
num = 'sss'
print("num is: num = 'sss' ", num, type(num))
