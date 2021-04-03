class Vertex:
    def __init__(self, label) -> None:
        super().__init__()
        self.label = label

    def __str__(self) -> str:
        return 'Vertex: ' + self.get_label()

    def __hash__(self) -> int:
        return hash(self.label)

    def get_label(self):
        return self.label
