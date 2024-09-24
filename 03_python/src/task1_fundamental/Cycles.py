print("Starting learn loop")

# Example of a while loop
count = 0
print("While loop:")
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment the count
print("---")

# Example of a while loop with else
count = 0
print("While loop with else:")
while count < 5:
    print(f"Count is: {count}")
    count += 1
else:
    print("Count reached 5!")
print("---")

# Example of a for loop
print("For loop:")
for i in range(5):
    print(f"Value is: {i}")
print("---")

# Example of a for loop with else
print("For loop with else:")
for i in range(5):
    print(f"Value is: {i}")
else:
    print("Completed looping through range!")
print("---")

# Example of using break
print("Break example:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 5
    print(f"Value is: {i}")
print("---")

# Example of using continue
print("Continue example:")
for i in range(5):
    if i == 2:
        print("Skipping value 2")
        continue  # Skip the rest of the loop when i equals 2
    print(f"Value is: {i}")
print("---")

# Example of using both break and continue
print("Break and Continue example:")
for i in range(6):
    if i == 4:
        print("Breaking the loop at i =", i)
        break
    elif i == 2:
        print("Skipping value 2")
        continue
    print(f"Value is: {i}")
print("---")

# Example of using pass
print("Pass example:")
for i in range(3):
    if i == 1:
        print("Value is 1, but doing nothing with it.")
        pass  # Placeholder for future code
    else:
        print(f"Value is: {i}")
print("---")
