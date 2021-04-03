from classes.Vertex import Vertex
from classes.Edge import Edge


class Graph:
    def __init__(self) -> None:
        super().__init__()
        self.adjacency_map = dict()
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
            if self.does_vertex_exist(label):
                print("The Vertex with label", label, "already exists")
            else:
                self.Vertices.append(Vertex(label))
        except AttributeError:
            self.Vertices = self.Vertices.append(Vertex(label))

    def does_vertex_exist(self, vertex_label):
        try:
            if len(self.Vertices) > 0:
                for v in self.Vertices:
                    if vertex_label == v.get_label():
                        return True
                return False
        except TypeError:
            return False

    def get_vertex_by_label(self, vertex_label):
        try:
            if len(self.Vertices) > 0:
                for v in self.Vertices:
                    if vertex_label == v.get_label():
                        return v
                return None
        except TypeError:
            return None

    def add_edge(self, source, destination):
        if self.does_vertex_exist(source) and self.does_vertex_exist(destination):
            self.Edges.append(Edge(self.get_vertex_by_label(source), self.get_vertex_by_label(destination)))
        else:
            print("Vertices:", source, destination, "do not exist")

    def generate_adj_dict(self):
        try:
            for v in self.Vertices:
                self.adjacency_map[v.get_label()] = []
            for e in self.Edges:
                self.adjacency_map[e.get_source().get_label()].append(e.get_destination())
        except TypeError:
            pass

    def print_adj_map(self):
        for vertex_label in self.adjacency_map.keys():
            print('Vertex', vertex_label, '->', end=" ")
            for edge in self.adjacency_map[vertex_label]:
                print(edge, end=", ")
            print("")
