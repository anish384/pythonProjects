# polymorphism 
# two ways to achieve polymorphism
# 1) inheritence
# 2) duck typing

# 1) inheritence

from abc import abstractmethod, ABC

# 1. THE CONTRACT (Abstract Base Class)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# 2. CONCRETE IMPLEMENTATIONS
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

# 3. MULTILEVEL INHERITANCE
# Pizza inherits from Circle, which inherits from Shape.
# Pizza acts exactly like a Circle regarding area(), so we don't need to rewrite it!
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

# 4. THE POLYMORPHIC BEHAVIOR
shapes = [Circle(4), Square(5), Pizza("pep", 5)]

# The loop treats them all as "Shapes". 
# It doesn't care if it's a Pizza or a Square, as long as it can call .area()
for shape in shapes:
    print(f"{shape.area()} cm^2")

# ****************************************************************************************************

# duck typing

class Circle:  # NO inheritance from Shape
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.14

class Square:  # NO inheritance from Shape
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width * self.width

# This creates a totally different object (not a shape), but it has an area!
class Carpet:
    def area(self):
        return 100

# ---------------------------------------
# POLYMORPHISM IN ACTION
# ---------------------------------------
objects = [Circle(4), Square(5), Carpet()]

for obj in objects:
    # Python does not check if these are "Shapes".
    # It simply checks: "Does this object have an .area() method?"
    # If yes -> Run it. 
    # If no -> Crash (AttributeError).
    print(f"{obj.area()} cm^2")


