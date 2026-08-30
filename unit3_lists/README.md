# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Reflection

During the completion of this assignment, I came to understand the effect of insertions, deletions, and searches on the structure and efficiency of the Python list. For instance, insertion at the first or mid-position would make other elements to move towards the right while deletions would result in a move to the left by the other elements. Also, I understood that linear search would involve checking of values up to the one that has been required or up to the end of the list.

The problem I encountered during the process was ensuring that deletion of elements does not raise an error due to an invalid index. I overcame this through the use of conditionals, which checked whether the index to be used in the pop method was valid. In addition, I tested my code on empty lists and non-existing values.

List efficiency is significant in practical applications where there are frequent additions, deletions, and searches of the data contained. For example, a contact list would use these three procedures in adding a new contact, deleting an outdated one, or searching for a person. However, if the list is very long, efficiency might suffer.
