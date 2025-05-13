def is_tournament(n, m, edges):
    if m != n * (n - 1) // 2:
        return False

    edge_set = set()
    for u, v in edges:
        if (v, u) in edge_set:
            return False
        edge_set.add((u, v))
    return True

def main():
    k = int(input())
    for _ in range(k):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        print("YES" if is_tournament(n, m, edges) else "NO")

if __name__ == "__main__":
    main()