class Vertex:
    def __init__(self, label) -> None:
        super().__init__()
        self.label = label

    def __str__(self) -> str:
        print('Vertex:', self.get_label())
        return ''

    def get_label(self):
        return self.label
