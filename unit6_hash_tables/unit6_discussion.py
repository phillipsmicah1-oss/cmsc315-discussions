"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # A Python dictionary works like a hash table by storing
    # key-value pairs. Each supply name is a unique key, and the
    # quantity is the value connected to that key.
    fish_tank_inventory = {}

    fish_tank_inventory["Minnows"] = 24
    fish_tank_inventory["Worms"] = 12
    fish_tank_inventory["Water Conditioner"] = 1
    fish_tank_inventory["Fish Food"] = 2
    fish_tank_inventory["Air Stones"] = 3

    print("Starting fish-tank supply inventory:")
    print(fish_tank_inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionary lookups use a key to quickly find its matching value.
    minnow_quantity = fish_tank_inventory["Minnows"]
    air_stone_quantity = fish_tank_inventory["Air Stones"]

    print("Minnows in inventory:", minnow_quantity)
    print("Air stones in inventory:", air_stone_quantity)

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before updating minnows:")
    print(fish_tank_inventory)

    # Assigning a new value to an existing key replaces the old value.
    # The dictionary does not create a duplicate "Minnows" key.
    fish_tank_inventory["Minnows"] = 18

    print("After updating minnows:")
    print(fish_tank_inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before removing worms:")
    print(fish_tank_inventory)

    # The del statement removes the key and its connected value
    # from the dictionary.
    del fish_tank_inventory["Worms"]

    print("After removing worms:")
    print(fish_tank_inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # get() safely looks up a missing key and returns None
    # instead of causing a KeyError.
    filter_quantity = fish_tank_inventory.get("Filter")
    print("Looking up a missing filter:", filter_quantity)

    # pop() with a default value safely attempts to remove a missing key.
    # Because "Heater" is not present, no error occurs.
    removed_heater = fish_tank_inventory.pop("Heater", None)
    print("Trying to remove a missing heater:", removed_heater)

    # Adding a key that was not previously in the dictionary creates
    # a new key-value pair.
    fish_tank_inventory["Fish Net"] = 1
    print("After adding a new fish net:", fish_tank_inventory)

    # Python handles collisions internally. If two keys produce the same
    # hash location, the dictionary still keeps the correct key-value pairs.
    print("\nHash tables make inventory lookups efficient because")
    print("a supply can be found by its key instead of checking every item.")


if __name__ == "__main__":
    main()