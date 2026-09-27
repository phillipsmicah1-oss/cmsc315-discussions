"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    Implements Bubble Sort by comparing adjacent values
    and swapping them when they are out of order.
    """

    # Create a copy so the original list is not changed
    sorted_list = lst.copy()

    # Move through the list multiple times
    for i in range(len(sorted_list)):

        # Track whether any values were swapped
        swapped = False

        for j in range(0, len(sorted_list) - i - 1):

            # Swap adjacent values if they are out of order
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )
                swapped = True

        # Stop early if the list is already sorted
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    Implements Merge Sort using recursion and
    divide-and-conquer.
    """

    # A list with zero or one item is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list
    middle = len(lst) // 2

    # Divide the list into two halves
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Sort both halves recursively
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves together
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare values from each list
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list
    result.extend(left[left_index:])

    # Add any remaining values from the right list
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 17, 8, 31, 25, 4, 19]

    print("Original List:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # DATASET #2
    # ===============================

    print("\n=== DATASET #2 ===")

    dataset2 = [90, 12, 76, 33, 58, 21, 45, 67]

    print("Original List:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort:", merge_sort(dataset2))

    print("\nBoth algorithms produced the same sorted result.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEmpty List:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Both algorithms return an empty list without errors.")

    # Edge Case 2: List with duplicate values
    duplicate_list = [5, 2, 5, 3, 2, 8, 5]

    print("\nDuplicate Values:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Duplicate values are kept and placed in the correct order.")

    # Edge Case 3: Reverse-sorted list
    reverse_list = [9, 8, 7, 6, 5, 4, 3]

    print("\nReverse-Sorted List:")
    print("Original:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))
    print("Both algorithms correctly sort a list that starts in reverse order.")

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD SORTING EXAMPLE ===")

    viewer_ratings = [4.8, 3.9, 4.5, 2.7, 4.9, 3.5, 4.2]

    print("Streaming Content Ratings:", viewer_ratings)
    print("Bubble Sort:", bubble_sort(viewer_ratings))
    print("Merge Sort:", merge_sort(viewer_ratings))

    print(
        "A streaming service could sort ratings to help organize "
        "content based on viewer scores."
    )


if __name__ == "__main__":
    main()