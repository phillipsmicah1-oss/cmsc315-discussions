# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior. My real-world example is a fish-tank supply inventory that stores supply names as keys and quantities as values.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements Completed

1. Created and populated a dictionary with fish-tank supplies.
2. Demonstrated lookup operations for minnows and air stones.
3. Updated the quantity of minnows.
4. Deleted worms from the inventory.
5. Tested edge cases by looking up and removing missing items safely.
6. Created a real-world inventory-management scenario.

## How the Program Works

The dictionary stores each supply name as a unique key and its quantity as the value. For example, `"Minnows"` is the key and `24` is its original value. Python uses hashing internally to locate a key’s value quickly. Updating a key replaces its old value instead of creating a duplicate. Deleting a key removes both the key and its associated value.

The program also handles missing items safely. Using `get()` for a missing key returns `None`, and using `pop()` with a default value prevents an error when attempting to remove an item that is not in the inventory.

## Discussion Board Reflection

Completing this assignment helped me better understand how Python dictionaries work like hash tables. I learned that a dictionary stores information as key-value pairs, which makes it useful for something like tracking fish-tank supplies. Instead of searching through every item one at a time, the program can use the supply name as a key to find its quantity quickly. I used insert, lookup, update, and delete operations to see how the dictionary changes during each step.

One challenge was making sure I used methods that would not cause an error when an item was missing. I handled this by using `get()` for a lookup and `pop()` with a default value when removing a missing item. That showed me how edge cases can be handled safely.

Hash tables are efficient because they use a hash value to help find where data is stored. A collision happens when different keys map to the same location internally. Python dictionaries handle collisions automatically, so the correct key-value pairs can still be retrieved. This makes dictionaries useful for fast inventory lookups and other applications that need quick access to data.