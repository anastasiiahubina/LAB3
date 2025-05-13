def is_tree(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n

    def dfs(v, parent):
        visited[v] = True
        for u in range(n):
            if adj_matrix[v][u]:
                if not visited[u]:
                    if not dfs(u, v):
                        return False
                elif u != parent:
                    return False
        return True

    # Перевірка кількості ребер
    edge_count = sum(sum(row) for row in adj_matrix) // 2
    if edge_count != n - 1:
        return False

    # Перевірка на цикли та зв'язність
    if not dfs(0, -1):
        return False
    if not all(visited):
        return False

    return True


def main():
    N = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]
    print("YES" if is_tree(adj_matrix) else "NO")


if __name__ == "__main__":
    main()