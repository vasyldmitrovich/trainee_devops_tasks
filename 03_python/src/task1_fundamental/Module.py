import sys
import re
# Importing specific functions from the math module with aliases
from math import sqrt as square_root, pow as power

# Using the alias for sqrt (square_root)
result1 = square_root(16)  # Equivalent to math.sqrt(16)
print(result1)  # Output: 4.0

# Using the alias for pow (power)
result2 = power(2, 3)  # Equivalent to math.pow(2, 3)
print(result2)  # Output: 8.0

print("---")


# This function will simply print a message when called
def main():
    print("This script is being run directly.")


# This function is for when the script is imported as a module
def module_function():
    print("This script has been imported as a module.")


# Now, we check the value of __name__
if __name__ == "__main__":
    # If this file is being run as a standalone script, __name__ will be "__main__"
    print("The __name__ variable is set to '__main__'.")
    main()  # Call the main function for standalone execution
else:
    # If this file is imported as a module, __name__ will be set to the module's name
    print(f"The __name__ variable is set to '{__name__}'.")
    module_function()  # Call a function to handle the imported case

# Output the module search path
print("Module search paths:")
for path in sys.path:
    print(path)

print("---")

# Sample text
text = "The rain in Spain falls mainly in the plain."

# Search for a pattern
# The \bin\b expression looks for the whole word 'in' (bounded by word boundaries \b)
pattern = r"\bin\b"

# Find all matches of the word 'in'
matches = re.findall(pattern, text)
print(f"Matches found: {matches}")  # Output: ['in', 'in']

# Replace all occurrences of 'in' with 'on'
# re.sub is used to replace a pattern with a new string
replaced_text = re.sub(pattern, "on", text)
print(f"Modified text: {replaced_text}")  # Output: The raon on Spaon falls maonly on the plaon.

# Compile the pattern to use multiple times
compiled_pattern = re.compile(r"\bfalls\b")

# Search for the word 'falls'
result = compiled_pattern.search(text)
if result:
    print(f"Found '{result.group()}' at position {result.start()}")  # Output: Found 'falls' at position 19
