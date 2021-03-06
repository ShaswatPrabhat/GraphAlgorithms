from classes.Graph import Graph


def generate_and_print_graph():
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_edge('a', 'b')
    g.add_edge('a', 'b')
    g.add_edge('a', 'b')
    print(g)
    g.generate_adj_dict()
    g.print_adj_map()


if __name__ == '__main__':
    generate_and_print_graph()
