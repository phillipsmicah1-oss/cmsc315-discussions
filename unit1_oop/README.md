# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Documentation

I created a parent class that represented a general vehicle and included class and instance variables for storing vehicle information. I then created a child class that represented a truck and inherited the make and model information from the parent class. The child class added bed length and towing capacity and overrode the `display_info()` method to provide more detailed information.

I demonstrated class and instance namespaces by creating two truck objects and displaying their `__dict__` values. I also added a color attribute to only one object to show how individual instances could contain different data.

I demonstrated shallow and deep copying using nested mutable data. The shallow copy shared the nested list with the original object, while the deep copy maintained its own separate copy. As a student-created extension, I added a `tow()` method to the child class that displayed when a truck was ready to tow.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.