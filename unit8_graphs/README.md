# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Implementation Summary

I created a graph using an adjacency list to represent
movie genres connected by similar viewing preferences.

I implemented BFS using a queue to visit nodes in the
order they were discovered. I also used a set to track
visited nodes and prevent them from being processed
more than once.

I started the traversal from Action and displayed
the order in which the genres were visited. I then
added Comedy to the graph and ran BFS again to
demonstrate how the traversal changed.

I tested three edge cases: an empty graph, a missing
starting node, and a graph containing only one node.
The program returned an empty list for the first
two cases and visited the only available node in
the third case.



## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

