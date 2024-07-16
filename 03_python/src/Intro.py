import io
import sys

print("Hello World")
# In separate lines
print("Hello "\
      "my friend")
"""
Print in separate lines
"""
print("Hello \nmy python") # Add new line

myvar1 = "Hello"
count = 3
print(f"{myvar1} new world, count is: {count}.")
var2 = 10
print("count + var2 = ", count + var2)
print("count - var2 = ", count - var2)
print("count * var2 = ", count * var2)
print("count / var2 = ", count / var2)
print("count module var2 = ", count % var2)
print("floor division count//var2 = ", count // var2)
print("exponent count**var2 = ", count ** var2)
print("------------------------")

number1 = 3 + 4 * 5 ** 2 + 7
print("3 + 4 * 5 ** 2 + 7 = ",number1)
number2 = (3 + 4) * (5 ** 2 + 7)
print("(3 + 4) * (5 ** 2 + 7) = ", number2)
number3 = 2**3**2
print("2**3**2 = ", number3)
number4 = (2**3)**2
print("(2**3)**2 = ", number4)
print('---','end block', '---', sep=" * ", end='!!!\n\n', flush=True)# forcibly flush the stream.

print("Wort with err")
# Save the current stderr
original_stderr = sys.stderr

# Create a temporary stream for errors
temp_stderr = io.StringIO()

# Redirect stderr to the temporary stream
sys.stderr = temp_stderr

print('---','This message is from error', '---', sep=" * ", file=sys.stderr)

# Get the content of the temporary stream
error_message = temp_stderr.getvalue()

# Restore the original stderr
sys.stderr = original_stderr

# Print the error message to stdout
print("Captured error message:", error_message)

print('---','new block with data from user', '---', sep=" ")

number = int(input("Input integer number: "))
print("Int num is:",number,type(number))
num = input("by default input number is string: ")
print("num is: ", num,type(num))
