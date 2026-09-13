"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check each value from the beginning of the list to the end.
    for index, value in enumerate(lst):
        if value == target:
            return index

    # The target was not found after checking the entire list.
    # Linear search has O(n) time complexity because it may check every item.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    while left<= right:
        # Check the middle value of the remaining search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            # Discard the left half of the search area.
            left = middle + 1
        else:
            # Discard the right half of the search area.
            right = middle - 1

    # The target was not found after the search area became empty.
    # Binary search has O(log n) time complexity.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # This sorted dataset allows both search algorithms to work correctly.
    small_dataset = [10, 20, 30, 40, 50]
    existing_target = 30
    missing_target = 35

    # Both searches should return index 2 for the existing value.
    print("Linear search for 30:", linear_search(small_dataset, existing_target))
    print("Binary search for 30:", binary_search(small_dataset, existing_target))

    # Both searches should return -1 because 35 is not in the list.
    print("Linear search for 35:", linear_search(small_dataset, missing_target))
    print("Binary search for 35:", binary_search(small_dataset, missing_target))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Create a sorted list containing 10,000 values.
    large_dataset = list(range(1, 10001))
    large_target = 9999

    linear_result = linear_search(large_dataset, large_target)
    binary_result = binary_search(large_dataset, large_target)

    print("Linear search result:", linear_result)
    print("Binary search result:", binary_result)

    # Both searches find the same index, but linear search may examine
    # almost every value. Binary search repeatedly cuts the search area
    # in half, making it more efficient as the dataset grows.
    print("Binary search is more efficient for this large sorted dataset.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge case 1: An empty list contains no searchable values,
    # so both algorithms should return -1.
    empty_list = []
    print("Linear search with empty list:", linear_search(empty_list, 10))
    print("Binary search with empty list:", binary_search(empty_list, 10))

    # Edge case 2: A single-element list should return index 0
    # when its only value matches the target.
    single_element = [42]
    print("Linear search with one matching item:",
          linear_search(single_element, 42))
    print("Binary search with one matching item:",
          binary_search(single_element, 42))

    # Real-world scenario: searching for a product ID in store inventory.
    print("\n=== REAL-WORLD INVENTORY SEARCH ===")

    product_ids = [1001, 1005, 1010, 1025, 1050]
    target_product = 1025

    print("Linear inventory search:",
          linear_search(product_ids, target_product))
    print("Binary inventory search:",
          binary_search(product_ids, target_product))

    # Linear search is practical for a short or unsorted inventory list.
    # Binary search is faster for a large inventory when the IDs are sorted.
if __name__ == "__main__":
    main()
