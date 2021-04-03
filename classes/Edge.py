from classes.Vertex import Vertex


class Edge:
    def __init__(self, source: Vertex, destination: Vertex, weight=0) -> None:
        super().__init__()
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return 'Source: ' + self.source.get_label() + ' Destination: ' + self.destination.get_label()

    def get_source(self) -> Vertex:
        return self.source

    def get_destination(self) -> Vertex:
        return self.destination
