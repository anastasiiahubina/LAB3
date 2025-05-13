from collections import deque

def topological_sort(n, edges):
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    # Побудова графа та підрахунок входів
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Черга з вершин без входів
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Якщо в результаті не всі вершини — є цикл
    if len(result) != n:
        return [-1]
    return result

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = topological_sort(n, edges)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()