"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insert() places the new value at the specified index.
    # Existing elements at that index and after it shift one position right.
    # Inserting near the beginning is slower because more elements must shift,
    # while inserting at the end usually requires little or no shifting.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Checking the index first prevents an IndexError and keeps deletion safe.
    # Only indexes from 0 through len(lst) - 1 are valid for this program.
    if 0 <= index < len(lst):
        # pop() removes the item at the index and returns the removed value.
        return lst.pop(index)

    # None indicates that the requested index did not exist.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because it examines each element sequentially,
    # beginning at index 0 and continuing until it finds the requested value.
    for index in range(len(lst)):
        if lst[index] == value:
            # Return the index immediately when the value is found.
            return index

    # Return -1 after the entire list has been scanned without finding the value.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create and display the original list.
    numbers = [20, 40, 60]
    print("Original list:", numbers)

    # Insert 10 at index 0, causing every existing element to shift right.
    insert_at(numbers, 0, 10)
    print("After inserting 10 at the beginning:", numbers)

    # Insert 30 at index 2, causing the elements after that index to shift right.
    insert_at(numbers, 2, 30)
    print("After inserting 30 in the middle:", numbers)

    # Insert 70 at the current length of the list to place it at the end.
    insert_at(numbers, len(numbers), 70)
    print("After inserting 70 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Delete the first item at index 0.
    removed_value = delete_at(numbers, 0)
    print("Removed from the beginning:", removed_value)
    print("List after beginning deletion:", numbers)

    # Calculate the middle index and delete the item stored there.
    middle_index = len(numbers) // 2
    removed_value = delete_at(numbers, middle_index)
    print("Removed from the middle:", removed_value)
    print("List after middle deletion:", numbers)

    # The final valid index is always one less than the list's length.
    removed_value = delete_at(numbers, len(numbers) - 1)
    print("Removed from the end:", removed_value)
    print("List after end deletion:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for 30, which currently exists in the list.
    search_result = search_value(numbers, 30)
    print("Searching for 30: found at index", search_result)

    # Search for 99, which is not in the list.
    search_result = search_value(numbers, 99)
    print("Searching for 99: result is", search_result)
    print("-1 means that the value was not found in the list.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Index 99 does not exist, so safe deletion returns None.
    invalid_deletion = delete_at(numbers, 99)
    print("Deleting at invalid index 99 returned:", invalid_deletion)
    print("The list remains unchanged:", numbers)

    # Edge case 2: Deleting from an empty list safely returns None.
    empty_list = []
    empty_deletion = delete_at(empty_list, 0)
    print("Deleting from an empty list returned:", empty_deletion)

    # Edge case 3: A value can be inserted at index 0 of an empty list.
    insert_at(empty_list, 0, 100)
    print("After inserting 100 into the empty list:", empty_list)



if __name__ == "__main__":
    main()
