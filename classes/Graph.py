class Graph:
    def __init__(self) -> None:
        super().__init__()
        vertices = list()
        edges = list()
        self.Vertices = vertices
        self.Edges = edges

    def __str__(self) -> str:
        print("Vertices:{} Edges:{}".format(self.Vertices, self.Edges))
        return super().__str__()
