class Student:
    # --- CLASS VARIABLES ---
    # These live inside the Class itself, not the individual objects.
    # There is only ONE copy of these variables in memory, shared by everyone.
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # --- INSTANCE VARIABLES ---
        # 'self' refers to the specific object being created (e.g., student1).
        # Every student gets their own separate copy of 'name' and 'age'.
        self.name = name
        self.age = age
        
        # Here we access the Class Variable to update the global counter.
        # We use 'Student.num_students' instead of 'self.num_students'
        # because we want to update the shared total, not a personal counter.
        Student.num_students += 1

# Creating instances (Objects)
student1 = Student('anish', 21) # num_students becomes 1
student2 = Student('sujal', 21) # num_students becomes 2
student3 = Student('mkdir', 22) # num_students becomes 3

# Accessing an Instance Variable (Unique to Anish)
print(student1.name) 
# Output: anish

# Accessing Class Variables
# You noted: "we should access class variables using directly the name of the class"
# This is best practice! It makes it clear this data is shared.
print(Student.class_year)
# Output: 2024

print(Student.num_students)
# Output: 3 (Because 3 objects were created, running __init__ 3 times)

print(f"my graduating class of {Student.class_year} has {Student.num_students} students")
