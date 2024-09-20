#

print("Studying OOP conceptions")


# Define a base class named Vehicle
class Vehicle:
    # Constructor to initialize the base class fields
    def __init__(self, make, model, year):
        self.make = make  # Manufacturer
        self.model = model  # Model of the vehicle
        self.year = year  # Manufacturing year

    # Method to display vehicle details
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

    # Method to simulate starting the vehicle
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is starting...")


# Define a derived class named Car, inheriting from Vehicle
class Car(Vehicle):
    # Constructor for the derived class
    def __init__(self, make, model, year, door_count):
        # Call the constructor of the parent class
        super().__init__(make, model, year)
        self.door_count = door_count  # Number of doors

    # Method specific to the Car class
    def open_doors(self):
        print(f"Opening {self.door_count} doors of the {self.make} {self.model}.")


# Create an instance of the base class Vehicle
my_vehicle = Vehicle("Honda", "Civic", 2021)
my_vehicle.display_info()  # Output: Vehicle Info: 2021 Honda Civic
my_vehicle.start_engine()  # Output: The Honda Civic's engine is starting...

# Create an instance of the derived class Car
my_car = Car("Tesla", "Model S", 2022, 4)
my_car.display_info()  # Output: Vehicle Info: 2022 Tesla Model S
my_car.start_engine()  # Output: The Tesla Model S's engine is starting...
my_car.open_doors()  # Output: Opening 4 doors of the Tesla Model S.
print("---")


class MyClass:
    "This is my second class"
    a = 10

    def func(self):
        print('Hello')


# create a new MyClass
firstobject = MyClass()
# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)
# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(firstobject.func)
# Calling function func()
# Output: Hello
firstobject.func()
print("---")


class Dog:
    def __init__(self, name, breed):
        # Initialize attributes name and breed
        self.name = name
        self.breed = breed

    def bark(self):
        # Method to simulate the dog barking
        print(f"{self.name} is barking!")

    def add_age(self, age):
        # Adds a new attribute 'age' to the object
        self.age = age
        print(f"{self.name} is {self.age} years old.")

    def remove_breed(self):
        # Removes the 'breed' attribute from the object
        del self.breed


# Create a Dog object
my_dog = Dog("Buddy", "Golden Retriever")

# Call the bark method
my_dog.bark()

# Add the 'age' attribute using the add_age method
my_dog.add_age(5)

# Remove the 'breed' attribute using remove_breed method
my_dog.remove_breed()

# Trying to access the 'breed' attribute after deletion will cause an error
try:
    print(my_dog.breed)
except AttributeError:
    print("Breed attribute has been removed.")
print("---")


class Rectangle:
    # Constructor to initialize the length and width
    def __init__(self, length, width):
        self.length = length  # Initialize length attribute
        self.width = width  # Initialize width attribute
        print(f"Rectangle created with length={self.length} and width={self.width}")

    # Method to calculate area of the rectangle
    def area(self):
        return self.length * self.width

    # Method to calculate perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Destructor to clean up when the object is deleted
    def __del__(self):
        print(f"Rectangle with length={self.length} and width={self.width} is being deleted")


# Creating an object of the Rectangle class
rect = Rectangle(5, 3)

# Calling methods
print(f"Area of the rectangle: {rect.area()}")
print(f"Perimeter of the rectangle: {rect.perimeter()}")

# Deleting the object (Destructor will be called)
del rect
print("---")


class Point:
    # Constructor to initialize x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator to add two points
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Method to display the point's coordinates
    def display(self):
        print(f"Point({self.x}, {self.y})")

    # Overloading the str() function for printing
    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Adding two points using the overloaded + operator
point3 = point1 + point2

# Displaying the result
print("point1:", point1)
print("point2:", point2)
print("Sum of point1 and point2 (point3):", point3)
print("---")

import math


class Circle:
    # Constructor to initialize the radius of the circle
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate the area of the circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate the circumference of the circle
    def circumference(self):
        return 2 * math.pi * self.radius

    # Overriding the __repr__ method for better object representation
    def __repr__(self):
        return f"Circle(radius={self.radius})"


# Creating a Circle object
circle = Circle(5)

# Printing the circle object and its area and circumference
print(circle)  # Output: Circle(radius=5)
print(f"Area: {circle.area()}")  # Output: Area: 78.53981633974483
print(f"Circumference: {circle.circumference()}")  # Output: Circumference: 31.41592653589793
print("---")


class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        # If no instance exists, create one
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # Initialize only if it's the first time
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True  # Mark as initialized

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


# Testing the Singleton
singleton1 = Singleton(10)
print(f"Singleton1 value: {singleton1.get_value()}")  # Output: Singleton1 value: 10

singleton2 = Singleton(20)
print(f"Singleton2 value: {singleton2.get_value()}")  # Output: Singleton2 value: 10

# Check if both instances are the same
print(singleton1 is singleton2)  # Output: True
print("---")


# Base class for geometric shapes
class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


# Triangle class that inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base  # Base of the triangle
        self.height = height  # Height of the triangle

    def area(self):
        # Calculate area of the triangle
        return 0.5 * self.base * self.height

    def __eq__(self, other):
        # Overloading the equality operator
        if isinstance(other, Triangle):
            return self.area() == other.area()
        return False


# Example usage
triangle1 = Triangle(10, 5)
triangle2 = Triangle(4, 12.5)

print(f"Area of triangle 1: {triangle1.area()}")  # Output: 25.0
print(f"Area of triangle 2: {triangle2.area()}")  # Output: 25.0

# Check if the two triangles have the same area
print(f"Are the triangles equal in area? {triangle1 == triangle2}")  # Output: True
print("---")


# Base class for birds
class Bird:
    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")


# Sparrow class that inherits from Bird
class Sparrow(Bird):
    def make_sound(self):
        return "Chirp!"


# Eagle class that inherits from Bird
class Eagle(Bird):
    def make_sound(self):
        return "Screech!"


# Function that demonstrates polymorphism
def bird_sound(bird):
    print(bird.make_sound())
    # Check if the bird is an instance of Bird
    if isinstance(bird, Bird):
        print(f"{bird.__class__.__name__} is an instance of Bird.")
    else:
        print(f"{bird.__class__.__name__} is NOT an instance of Bird.")


# Example usage
sparrow = Sparrow()
eagle = Eagle()

# Check if classes are subclasses of Bird
print(f"Sparrow is subclass of Bird: {issubclass(Sparrow, Bird)}")  # Output: True
print(f"Eagle is subclass of Bird: {issubclass(Eagle, Bird)}")  # Output: True

# Calling the same method on different objects
print("Calling the same method on different objects")
bird_sound(sparrow)  # Output: Chirp!
bird_sound(eagle)  # Output: Screech!
print("---")


# Base class for flying
class Flyer:
    def fly(self):
        return "I can fly!"


# Base class for swimming
class Swimmer:
    def swim(self):
        return "I can swim!"


# Derived class that inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"


# Function to demonstrate the capabilities of the Duck
def demonstrate_duck(duck):
    print(duck.quack())  # Call the quack method
    print(duck.fly())  # Call the fly method from Flyer
    print(duck.swim())  # Call the swim method from Swimmer


# Example usage
if __name__ == "__main__":
    duck = Duck()
    demonstrate_duck(duck)

    # Check the class hierarchy
    print(f"{Duck.__name__} is a subclass of {Flyer.__name__}: {issubclass(Duck, Flyer)}")  # True
    print(f"{Duck.__name__} is a subclass of {Swimmer.__name__}: {issubclass(Duck, Swimmer)}")  # True
print("---")


class Employee:
    # Static variable to keep track of the number of employees
    employee_count = 0

    def __init__(self, name, position):
        self.name = name  # Instance variable for employee's name
        self.position = position  # Instance variable for employee's position
        Employee.employee_count += 1  # Increment the static variable

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count  # Return the current employee count

    def display_info(self):
        # Display employee information
        return f"Name: {self.name}, Position: {self.position}"


# Example usage
if __name__ == "__main__":
    emp1 = Employee("Alice", "Developer")
    emp2 = Employee("Bob", "Manager")

    # Displaying individual employee information
    print(emp1.display_info())
    print(emp2.display_info())

    # Displaying the total number of employees
    print(f"Total number of employees: {Employee.get_employee_count()}")
print("---")


class MathOperations:
    # Static method to add two numbers
    @staticmethod
    def add(x, y):
        return x + y

    # Class method to create an instance with a default value
    @classmethod
    def create_with_default(cls):
        return cls(0)  # Create an instance with a default value of 0

    def __init__(self, value):
        self.value = value  # Instance variable

    def display_value(self):
        return f"Value: {self.value}"


# Example usage
if __name__ == "__main__":
    # Using the static method to add two numbers
    result = MathOperations.add(5, 10)
    print(f"Result of addition: {result}")

    # Creating an instance using the class method
    default_instance = MathOperations.create_with_default()
    print(default_instance.display_value())
print("---")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public variable
        self.__balance = balance  # Private variable

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    # Method to get the current balance
    def get_balance(self):
        return self.__balance


# Example usage
if __name__ == "__main__":
    account = BankAccount("Alice", 100)

    # Accessing public variable
    print(f"Account owner: {account.owner}")

    # Depositing money
    account.deposit(50)

    # Attempting to access private variable (will raise an AttributeError)
    try:
        print(account.__balance)
    except AttributeError as e:
        print(f"Error: {e}")

    # Accessing balance using the public method
    print(f"Current balance: {account.get_balance()}")

    # Withdrawing money
    account.withdraw(30)

    # Final balance
    print(f"Final balance: {account.get_balance()}")
print("---")
