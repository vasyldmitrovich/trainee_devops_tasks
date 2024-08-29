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
    print("score > 8 You have passed the exam")
print("score not > 8 Exam was finished.")

# temperature = float(input('What is the temperature? '))
temperature = 37
if temperature > 30:
    print('temperature > 30 Wear shorts.')
else:
    print('else temperature < 30 Wear long pants.')
print('Get some exercise outside.\n')

age = 31
if age < 12:
    print('if age < 12 kid')
elif age < 18:
    print('elif age < 18 teenager')
elif age < 50:
    print('elif age < 50 adult')
else:
    print('else you are not old')

score = 58
if score >= 90:
    letter = 'if score >= 90 A'
elif score >= 80:
    letter = 'elif score >= 80 B'
elif score >= 70:
    letter = 'elif score >= 70 C'
elif score >= 60:
    letter = 'elif score >= 60 D'
else:
    letter = 'else F'
print("letter is: ", letter)

weather = "raining"
print(f"Ternary operator, weather={weather}, and ternary operator: ", "'Open Your umbrella' if weather == 'raining' else 'Wear your cap'")
print("Open Your umbrella" if weather == "raining" else "Wear your cap\n-----")

status = 555
print(f"match case checking variable status = {status}")
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
print(f"Set variable status={status}", " and use case 401 | 403 as error")
match status:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f"{error} is authentication error")
    case 404:
        print("Not found")
    case _:
        print("Other error")

item = ['evening', 'read a book']
#item = ['morning', 'exercise']
# item = ['night', 'sleep']
# item = ['evening', 'have dinner']
print("Using match case with list, check first element and set second element to temp var\n", "item = ['evening', 'read a book']",
      "case ['evening', action]")
match item:
    case ['evening', action]:
        print(f'You almost finished the day! Now {action}!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}')
    case _:
        print("The time is invalid.")

print("---\n")


