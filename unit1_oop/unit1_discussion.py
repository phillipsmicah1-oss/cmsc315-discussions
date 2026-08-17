"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    vehicle_type = "Vehicle"

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    vehicle_category = "Truck"

    def __init__(self, make, model, bed_length, towing_capacity):
        super().__init__(make, model)
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity

    def display_info(self):
        return (
            f"{self.make} {self.model} - "
            f"Bed Length: {self.bed_length} ft, "
            f"Towing Capacity: {self.towing_capacity} lbs"
        )

    def tow(self):
        return f"{self.make} {self.model} is ready to tow."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    truck1 = ChildClass("Ford", "F-150", 5.5, 10000)
    truck2 = ChildClass("Chevrolet", "Silverado", 6.5, 9500)

    print("Class variable through class:", ChildClass.vehicle_category)
    print("Class variable through object:", truck1.vehicle_category)

    truck1.color = "Blue"

    print("\nTruck 1 namespace:")
    print(truck1.__dict__)

    print("\nTruck 2 namespace:")
    print(truck2.__dict__)

    print("\nChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass("Ford", "F-150", 5.5, 10000)
    original.tools = ["Jack", "Wrench", ["Socket Set", "Screwdriver"]]

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new object, but nested mutable data
    # is still shared with the original object.
    # A deep copy creates a completely separate copy,
    # including all nested mutable data.

    original.tools[2].append("Pliers")

    print("Original object tools:")
    print(original.tools)

    print("\nShallow copy tools:")
    print(shallow_copy.tools)

    print("\nDeep copy tools:")
    print(deep_copy.tools)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    vehicle = ParentClass("Toyota", "Camry")
    print(vehicle.display_info())

    print("\n=== Child Object ===")
    truck = ChildClass("Ford", "F-150", 5.5, 10000)
    print(truck.display_info())
    print(truck.tow())

    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()