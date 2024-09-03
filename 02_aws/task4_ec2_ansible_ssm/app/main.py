# src/main.py
from calculator import Calculator

def main():
    calc = Calculator()
    result = calc.add(5, 10)
    print(f"The result of addition is: {result}")

if __name__ == "__main__":
    main()
