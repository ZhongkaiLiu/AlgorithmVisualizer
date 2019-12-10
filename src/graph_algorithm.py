from panel import Panel
import graph_cross
import graph_point


class GraphAlgorithm(object):

    def __init__(self, node_shape, duration, root):
        self.screen = Panel()
        if (node_shape == "cross"):
            self.graph = graph_cross.Graph(self.screen)
        else:
            self.graph = graph_point.Graph(self.screen)
        self.graph.set_duration(duration)
        self.graph.set_root(root)

    # display the initial graph on the panel
    def display_init(self):
        self.graph.draw_large_graph()
        self.graph.display_graph(2)

    def bfs(self):
        self.display_init()
        self.graph.bfs_start()
        self.graph.display_graph(2)
        self.screen.clean_gpio()

    def dfs(self):
        self.display_init()
        self.graph.dfs_start()
        self.graph.display_graph(2)
        self.screen.clean_gpio()
