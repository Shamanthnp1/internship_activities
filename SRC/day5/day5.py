def greet():
    print("hello,welcome to the internship!")
greet()

#arguments and return values
def add_numbers(a,b):
    return a+b
result = add_numbers(5,3)
print("the sum is:",result)

#variable scope
x=10
def show_value():
    x=5
    print(x)
show_value()
print(x)

#importing modules
import math
import random
print(math.sqrt(16))
print(random.randint(1,10))#unform for random float between 1 and 10


#creating custom modules
import utils
print(utils.multiply(3,4))


#function to calculate area and perimeter of a rectangle
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")
