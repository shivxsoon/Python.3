import math

class Circle:
    # Constructor to initialize the radius
    def __init__(self, radius):
        self.radius = radius

    #  calculate area
    def area(self):
        return math.pi * (self.radius ** 2)

    #  calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# --- Main program ---
# Taking user input for radius
r = float(input("Enter the radius of the circle: "))

# Creating an object of the Circle class
circle1 = Circle(r)

# Displaying results
print(f"The area of the circle is: {circle1.area():.2f}")
print(f"The perimeter (circumference) of the circle is: {circle1.perimeter():.2f}")
