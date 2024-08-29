# src/main.py
from calculator import Calculator
from greeter import Greeter

def main():
    calc = Calculator()
    result = calc.add(5, 10)
    print(f"The result of addition is: {result}")

    greet = Greeter()
    message = greet.say_hello("John")
    print(message)

if __name__ == "__main__":
    main()
