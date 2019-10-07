"""HW8 - Task 3

Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:

- граф должен храниться в виде списка смежности;
- генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random


def create_graph(vertex, percent=1.0):
    assert 0 < percent <= 1, 'wrong percent'
    graph = {}

    for i in range(vertex):
        graph[i] = set()
        count_edge = random.randrange(1, int(vertex * percent))
        while len(graph[i]) < count_edge:
            edge = random.randrange(0, vertex)
            if edge != i:
                graph[i].add(edge)

    return graph


def gen_adj_list(n):
    adjacency_list = []
    for vertex in range(n):
        adjacency_list.append(random.sample([v for v in range(n) if vertex != v], k=random.randint(0, n - 1)))
    return adjacency_list


def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path


def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path


adjacency_list = gen_adj_list(8)
print(adjacency_list)
print(dfs_recursive(adjacency_list, 0))
