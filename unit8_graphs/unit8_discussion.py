
"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting node does not exist.
    if start not in graph:
        return []

    # A queue processes nodes in the order they are added (FIFO).
    queue = deque([start])
    visited = {start}
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        # Add unvisited neighbors to explore the next level.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS explores nearby nodes before moving deeper,
    # while DFS follows one path before backtracking.
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Nodes represent movie genres on a streaming platform.
    # Edges connect genres with similar viewing preferences.
    graph = {
        "Action": ["Sci-Fi", "Thriller"],
        "Sci-Fi": ["Action", "Fantasy"],
        "Thriller": ["Action", "Drama"],
        "Fantasy": ["Sci-Fi"],
        "Drama": ["Thriller", "Documentary"],
        "Documentary": ["Drama"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    # Start with Action and explore its closest connections first.
    start = "Action"
    print("Starting node:", start)
    print("Traversal order:", bfs(graph, start))

    # Add a new genre and connect it to Drama.
    graph["Comedy"] = ["Drama"]
    graph["Drama"].append("Comedy")

    print("\nAfter adding Comedy:")
    print("Updated traversal:", bfs(graph, start))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty graph has no nodes to visit.
    empty_graph = {}
    print("Empty graph:", bfs(empty_graph, "Action"))

    # Edge case 2: A missing starting node returns an empty list.
    print("Missing start node:", bfs(graph, "Horror"))

    # Edge case 3: A graph with one node visits that node only.
    single_graph = {"Comedy": []}
    print("Single-node graph:", bfs(single_graph, "Comedy"))


if __name__ == "__main__":
    main()
