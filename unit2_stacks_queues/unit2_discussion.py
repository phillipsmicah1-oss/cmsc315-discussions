"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items =[]

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The newest value is added to the top so it can be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return None
        # Peek returns the newest value without removing it from the stack
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so the oldest value leaves first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return None
        # Front returns the oldest value without removing it from the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    stack = Stack()
    print("\n=== STACK DEMO ===")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Added to stack in order: 10,20,30,40")
    print("Removed from stack:", stack.pop())
    print("Next value removed:", stack.pop())
    print("Next value removed:", stack.pop())
    print("Last value removed:", stack.pop())
    print("Pop from empty stack:", stack.pop())
    print("Peek at empty stack:", stack.peek())
    single_stack = Stack()
    single_stack.push(99)
    print("Single stack item removed:", single_stack.pop())
    print("Is single-item stack empty now?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    queue = Queue()
    print("\n=== QUEUE DEMO ===")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print("Added to queue in order: 10, 20, 30, 40")
    print("Removed from queue:", queue.dequeue())
    print("Next value removed:", queue.dequeue())
    print("Next value removed:", queue.dequeue())
    print("Last value removed:", queue.dequeue())
    print("Dequeue from empty queue:", queue.dequeue())
    print("Front of empty queue:", queue.front())
    single_queue = Queue()
    single_queue.enqueue(99)
    print("Single queue item removed:", single_queue.dequeue())
    print("Is single-item queue empty now?", single_queue.is_empty())

    print("\n=== REAL-WORLD SCENARIO ===")
    undo_history = Stack()
    undo_history.push("Typed a sentence")
    undo_history.push("Deleted a word")
    undo_history.push("Changed the font")
    print("Undo removed:", undo_history.pop())

    customer_line = Queue()
    customer_line.enqueue("Customer 1")
    customer_line.enqueue("Customer 2")
    customer_line.enqueue("Customer 3")
    print("First customer served:", customer_line.dequeue())
    print("Next customer waiting:", customer_line.front())



if __name__ == "__main__":
    main()
