from classes.Vertex import Vertex


class Edge:
    def __init__(self, source, destination, weight=0) -> None:
        super().__init__()
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return 'Source: ' + self.source + ' Destination: ' + self.destination

    def get_source(self) -> Vertex:
        return self.source

    def get_destination(self) -> Vertex:
        return self.destination
