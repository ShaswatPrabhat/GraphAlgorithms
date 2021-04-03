class Edge:
    def __init__(self, source, destination, weight=0) -> None:
        super().__init__()
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self) -> str:
        print('Source:', self.source, 'Destination:', self.destination)
        return ''
