print("--- Start working with condition statement ---")

x1 = 5
x2 = 5
print("x1=5 is x2=5: ", x1 is x2)
x1list = [1, 2, 3]
x2list = [1, 2, 3]
print("x1list = [1,2,3] is x2list = [1,2,3]: ", x1list is x2list)
print("x1list = [1,2,3] == x2list = [1,2,3]: ", x1list == x2list)

x = 'Hello World'
y = {1: 'a', 2: 'b'}
print("H in x", 'H' in x)
print("'hello' not in x", 'hello' not in x)
print("1 in y", 1 in y)
print("'a' in y", 'a' in y)

score = 12
if score > 8:
    print("You have passed the exam")
print("Exam was finished.")

# temperature = float(input('What is the temperature? '))
temperature = 37
if temperature > 30:
    print('Wear shorts.')
else:
    print('Wear long pants.')
print('Get some exercise outside.\n')

age = 31
if age < 12:
    print('kid')
elif age < 18:
    print('teenager')
elif age < 50:
    print('adult')
else:
    print('you are not old')

score = 58
if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'
print("leter is: ", letter)

weather = "raining"
print("Open Your umbrella" if weather == "raining" else "Wear your cap")

status = 555
match status:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not found")
    case _:
        print("Other error")

status = 403
match status:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f"{error} is authentication error")
    case 404:
        print("Not found")
    case _:
        print("Other error")

#item = ['evening', 'read a book']
item = ['morning', 'exercise']
# item = ['night', 'sleep']
# item = ['evening', 'have dinner']
match item:
    case ['evening', action]:
        print(f'You almost finished the day! Now {action}!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}')
    case _:
        print("The time is invalid.")



