# Basics of Python 3

# Variables and data types
name = "John" # string
age = 30 # integer
height = 1.75 # float
is_student = True # boolean

# Operators
result = 2 + 3 # addition
result = 3 - 1 # subtraction
result = 4 * 2 # multiplication
result = 10 / 2 # division
result = 9 % 2 # modulo
result = 2 ** 3 # exponentiation
result = 10 // 3 # floor division

# String manipulation
message = "Hello, World!"
print(message.lower()) # "hello, world!"
print(message.upper()) # "HELLO, WORLD!"
print(message.count("l")) # 3
print(message.replace("World", "Python")) # "Hello, Python!"

# Control flow
if age < 18:
    print("You are not old enough to vote.")
elif age >= 18 and age < 21:
    print("You are old enough to vote but not to drink.")
else:
    print("You are old enough to vote and to drink.")

# Loops
for i in range(10):
    print(i)

while age < 40:
    age += 1

# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("John") # "Hello, John!"

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[1]) # "banana"
fruits.append("orange")
fruits.remove("banana")
print(fruits) # ["apple", "cherry", "orange"]

# Dictionaries
person = {"name": "John", "age": 30, "is_student": True}
print(person["name"]) # "John"
person["age"] += 1
print(person) # {"name": "John", "age": 31, "is_student": True}

# Tuples
point = (2, 3)
x, y = point
print(x, y) # 2 3

# Sets
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(4)
print(numbers) # {1, 2, 3, 5, 6}

# Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")

# File handling
with open("file.txt", "w") as f:
    f.write("Hello, World!")

with open("file.txt", "r") as f:
    print(f.read()) # "Hello, World!"

# Advanced Python 3

# Object-oriented programming
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person = Person("John", 30)
person.greet() # "Hello, my name is John and I am 30 years old."

# Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print("I am studying and getting good grades.")

student = Student("Jane", 20, 10)
student.greet() # "Hello, my name is Jane and I am 20 years old."
student.study() # "I am studying and getting good grades."

# Polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()
make_animal_sound(dog) # "Bark!"
make_animal_sound(cat) # "Meow!"

# Generators
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(5):
    print(i) # 0 1 2 3 4

# Decorators
def my_decorator(func):
    def wrapper():
        print("Before function call.")
        func()
        print("After function call.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() # "Before function call. Hello! After function call."

# Context managers
class MyContextManager:
    def __enter__(self):
        print("Entering context.")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context.")

with MyContextManager():
    print("Inside context.")

# Threading
import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()

# Async programming
import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1
    await task2

asyncio.run(main())

# Type hints
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(2, 3) # 5

# examples lambdas

# Lambda with one argument
f = lambda x: x**2
result = f(5) # 25

# Lambda with multiple arguments
g = lambda x, y: x + y
result = g(2, 3) # 5

# Lambda with default argument
h = lambda x, y=2: x + y
result = h(3) # 5

# Lambda with variable arguments
i = lambda *args: sum(args)
result = i(1, 2, 3, 4, 5) # 15

# Lambda with dictionary
j = lambda **kwargs: kwargs
result = j(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3}

# Sorting a list with a lambda
my_list = [(1, 2), (3, 1), (5, 3), (2, 4)]
my_list.sort(key=lambda x: x[1])
# my_list is now [(3, 1), (1, 2), (5, 3), (2, 4)]

# Filtering a list with a lambda
my_list = [1, 2, 3, 4, 5]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
# filtered_list is now [2, 4]

# Mapping a list with a lambda
my_list = [1, 2, 3, 4, 5]
mapped_list = list(map(lambda x: x**2, my_list))
# mapped_list is now [1, 4, 9, 16, 25]
