# class Circle:
#     def __init__(self, color, is_filled, radius):
#         self.color = color
#         self.is_filled = is_filled
#         self.radius = radius
#
# class Square:
#     def __init__(self, color, is_filled, width):
#         self.color = color
#         self.is_filled = is_filled
#         self.width = width
#
# class Rectangle:
#     def __init__(self, color, is_filled, width, height):
#         self.color = color
#         self.is_filled = is_filled
#         self.width = width
#         self.height = height

"""
in above code
we can see that self.color and self.is_filled is common 
here is where super() concept comes in
"""

# 1. THE PARENT (Base Class)
# Handles the logic common to ALL shapes.
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        # A generic description valid for any shape
        print(f"The Shape's color is {self.color} and is {'filled' if self.is_filled else 'not filled'}")

# 2. THE CHILDREN (Derived Classes)

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # --- USING SUPER IN __INIT__ ---
        # We take the arguments 'color' and 'is_filled' and pass them UP to the Parent.
        # The Shape class handles assigning them to self.color and self.is_filled.
        super().__init__(color, is_filled)
        
        # Now we handle the part that is unique to Circle.
        self.radius = radius

    def describe(self):
        # --- EXTENDING A METHOD ---
        # We want the Parent's description logic AND our own custom logic.
        # 1. Run the code inside Shape.describe()
        super().describe()
        
        # 2. Run the code specific to Circle
        # (Note: You calculated Area here, so I updated the text to say 'Area')
        print(f"The Circle Area is {3.14 * self.radius * self.radius} cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        # Pass common data to Shape, keep unique data (width) here
        super().__init__(color, is_filled)
        self.width = width

class Rectangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

# 3. EXECUTION
circle = Circle("red", False, 5)

# This works because 'super()' ensured 'self.color' was created in the Shape class
print(circle.color) 

# This calls the Circle version of describe(), which internally calls the Shape version
circle.describe()
