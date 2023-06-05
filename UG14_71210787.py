class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def vertex(self):
        print("\nSeluruh Node = ", end="")
        for key in self._data:
            print(key, end=" ")
        print()

    def edge(self):
        print("Seluruh Edge = ", end="")
        visited = set()
        for vertex in self._data:
            for neighbor in self._data[vertex]:
                if (neighbor, vertex) not in visited:
                    print(f"({vertex}, {neighbor})", end=" ")
                    visited.add((vertex, neighbor))
        print()

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)

    def bfs(self, node):
        visited = set()
        queue = [node]
        print("Hasil BFS Traversal:")
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self._data[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print("\n")

# Membuat graf sesuai dengan gambar yang diberikan
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('c', 'e')
graph.addEdge('b', 'c')
graph.addEdge('d', 'e')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('e', 'f')
graph.addEdge('a', 'b')

# Menampilkan vertex dan edge dari graf
graph.vertex()
graph.edge()

# Melakukan BFS traversal dari node 'a'
graph.bfs('a')
