#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:47:46 2024

@author: monikasameer
"""
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(sorted(self.graph[node], reverse=True))

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(sorted(self.graph[node], reverse=True))

    def has_cycle(self, node, visited, stack, rec_stack):
        visited.add(node)
        stack.add(node)
        rec_stack.add(node)

        neighbors = self.graph[node]
        i = 0
        while i < len(neighbors):
            neighbor = neighbors[i]
            if neighbor not in visited:
                if self.has_cycle(neighbor, visited, stack, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
            else:
                i += 1

        stack.remove(node)
        rec_stack.remove(node)
        return False

    def print_cycles(self):
        visited = set()
        stack = set()

        def print_cycle_util(node):
            stack.add(node)

            neighbors = self.graph[node]
            i = 0
            while i < len(neighbors):
                neighbor = neighbors[i]
                if neighbor in stack and neighbor not in visited:
                    print_cycle = list(stack)
                    start_index = print_cycle.index(neighbor)
                    print("Cycle:", end=' ')
                    print(*print_cycle[start_index:], end=' ')
                    print()
                    return
                if neighbor not in stack and neighbor not in visited:
                    print_cycle_util(neighbor)
                i += 1

            stack.remove(node)

        nodes = list(self.graph.keys())
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if node not in visited:
                print_cycle_util(node)
            i += 1

    def is_bipartite(self):
        visited = set()
        colors = {}

        nodes = list(self.graph.keys())
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if node not in visited:
                if not self.bfs_bipartite(node, visited, colors):
                    return False
            i += 1

        return True

    def bfs_bipartite(self, start_node, visited, colors):
        queue = deque([start_node])
        visited.add(start_node)
        colors[start_node] = 0

        while queue:
            node = queue.popleft()

            neighbors = self.graph[node]
            i = 0
            while i < len(neighbors):
                neighbor = neighbors[i]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    colors[neighbor] = 1 - colors[node]
                elif colors[neighbor] == colors[node]:
                    return False
                i += 1

        return True


# Example usage:
g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 2)

print("DFS:")
g.dfs(1)
print("\nBFS:")
g.bfs(1)

g.print_cycles()

if g.is_bipartite():
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
