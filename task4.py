def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w, i))  # додаємо індекс ребра

    total_weight = sum(edge[2] for edge in edges)

    # Ребро з максимальною вагою і найбільшим індексом
    max_weight = max(edge[2] for edge in edges)
    max_edge = max((e for e in edges if e[2] == max_weight), key=lambda x: x[3])

    # Ребро з мінімальною вагою і найменшим індексом
    min_weight = min(edge[2] for edge in edges)
    min_edge = min((e for e in edges if e[2] == min_weight), key=lambda x: x[3])

    print(total_weight)
    print(max_edge[0], max_edge[1], max_edge[2])
    print(min_edge[0], min_edge[1], min_edge[2])

if __name__ == "__main__":
    main()