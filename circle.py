import math
#Write a Python class named Point3D defined by x, y, and z. Define a method that returns (x, y ,z). This tells Python to represent this object in the following format: (x, y, z). Then create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3 and print it.
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        return (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print(my_point.get_coordinates())

#Write a Python class named Rectangle constructed by a length and width. Define two methods, area and perimeter, which will compute the area and the perimeter of the rectangle. Then create a variable named my_rectangle containing a new instance of Rectangle with width=3 and length = 4 and compute both area and perimeter ( the area is expected to be 3*4=12 and perimeter 2*(3+4)=14).
class Rectangle:
    definit__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(4, 3)
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())
#Write a Python  class named Circle constructed by its center O and radius r. Define two methods, area and perimeter, which will compute the area and the perimeter of the circle, and is Inside() method which allows you to test whether a point A(x, y) belongs to the circle C(O, r) or not.


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_inside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)
        return distance <= self.radius

my_circle = Circle(0, 0, 5print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
print("Is (3, 4) inside the circle?", my_circle.is_inside(3, 4))

#Suppose we want to model a bank account with support for deposit and withdraw operations. Let’s create a Python class named Bank defined by its balance. Define two methods, deposit and withdraw, to compute the new amount of each operation.


class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            printInsufficient funds.")
    
    def get_balance(self):
        return self.balance

my_bank = Bank(1000)
printInitial balance:", my_bank.get_balance())
my_bank.deposit(500)
print("Balance after deposit:", my_bank.get_balance())
my_bank.withdraw(200)
print("Balance after withdrawal:", my_bank.get_balance())
