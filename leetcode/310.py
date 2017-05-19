#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?
Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = self.build_graph(n, edges)
        min_height = float('inf')
        res = []
        for node in graph:
            if len(graph[node]) == 2:
                continue

            height = self.bfs(graph, node)
            if height < min_height:
                min_height = height
                res = [node]

            if height == min_height:
                res.append(node)

        return res

    def bfs(self, graph, node):
        queue = [node]
        visited = {node}
        dist = {}
        dist[node] = 0

        max_height = float('-inf')

        while len(queue) != 0:
            node = queue.pop(0)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

                    if dist[neighbor] > max_height:
                        max_height = dist[neighbor]

        return max_height

    def build_graph(self, n, edges):
        graph = {}

        for i in range(n):
            graph[i] = set()

        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].add(end)
            graph[end].add(start)

        return graph


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1: return [0]

        graph = self.build_graph(n, edges)

        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                end = graph[leaf].pop()
                graph[end].remove(leaf)
                if len(graph[end]) == 1:
                    new_leaves.append(end)

            leaves = new_leaves

        return leaves

    def build_graph(self, n, edges):
        graph = {}

        for i in range(n):
            graph[i] = set()

        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].add(end)
            graph[end].add(start)

        return graph



