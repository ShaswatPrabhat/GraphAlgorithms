from classes.Vertex import Vertex
from classes.Edge import Edge


class Graph:
    def __init__(self) -> None:
        super().__init__()
        self.Vertices = list()
        self.Edges = list()

    def __str__(self) -> str:
        try:
            print("Vertices:")
            for v in self.Vertices:
                print(v.get_label())
            print("Edges:")
            for e in self.Edges:
                print(e)
        except TypeError:
            pass
        return ''

    def add_vertex(self, label):
        try:
            if self.vertex_exists(label):
                print("The Vertex with label", label, "already exists")
            else:
                self.Vertices.append(Vertex(label))
        except AttributeError:
            self.Vertices = self.Vertices.append(Vertex(label))

    def vertex_exists(self, vertex_label):
        try:
            if len(self.Vertices) > 0:
                for v in self.Vertices:
                    if vertex_label == v.get_label():
                        return True
                return False
        except TypeError:
            return False

    def add_edge(self, source, destination):
        if self.vertex_exists(source) and self.vertex_exists(destination):
            self.Edges.append(Edge(source, destination))
        else:
            print("Vertices:", source, destination, "do not exist")
