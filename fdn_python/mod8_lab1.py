"""

Mod 8 - Lab 

Create a calculator

"""

# Create a class called "Calculate"
class Calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add method to add two numbers
    def add_two(self):
        sum = self.x + self.y
        return sum

    # Add method to subtract two numbers
    def subtract_two(self):
        difference = self.x - self.y
        return difference

    # Add method to divide two numbers
    def divide_two(self):
        remainder = self.x / self.y
        return remainder

    # Add method to multiplself.y two numbers
    def multiply_two(self):
        product = self.x * self.y
        return product

# Instantiate the class and use each method
num_set1 = Calculate(5,10)
print(num_set1.x, ",", num_set1.y)
num_set1.add_two()
print(num_set1.add_two())
print(num_set1.subtract_two())
print(num_set1.divide_two())
print(num_set1.multiply_two())

print()

num_set2 = Calculate(4,40)
print(num_set2.x, ",", num_set2.y)
num_set2.add_two()
print(num_set2.add_two())
print(num_set2.subtract_two())
print(num_set2.divide_two())
print(num_set2.multiply_two())
