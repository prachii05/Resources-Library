from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []

        visited[start] = True
        queue.append(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)

    print("Breadth-First Traversal (starting from vertex 0):", end=" ")
    g.bfs(0)

if __name__ == "__main__":
    main()
