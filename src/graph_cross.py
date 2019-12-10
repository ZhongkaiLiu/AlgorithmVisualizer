from panel import Panel
from node_cross import GraphNode
from collections import deque


class Graph(object):
    def __init__(self, screen):
        if (not isinstance(screen, Panel)):
            raise ValueError("screen must be an object of class Panel!")
        else:
            self.screen = screen
            self.adjlist = []
            self.nodes = []
            self.edges = []
            self.node_num = 0
            self.edge_num = 0
            self.root = None
            self.duration = 1

            # set node_color to WHITE as default
            self.node_color = 3
            # set edge_color to GREEN as default
            self.edge_color = 7
            # set visited node color to RED as default
            self.visited_node_color = 1
            # set visited edge color to GREEN as default
            self.visited_edge_color = 2

    def set_duration(self, duration):
        self.duration = duration

    # set node and line color of this graph
    # avoid setting color after having nodes or lines
    def set_color(self, node_color, edge_color, visited_node_color, visited_edge_color):
        self.node_color = node_color
        self.edge_color = edge_color
        self.visited_node_color = visited_node_color
        self.visited_edge_color = visited_edge_color

    # return a new node at (x, y)
    def new_node(self, x, y):
        return GraphNode(x, y, self.node_color, self.edge_color, self.screen, self.node_num)

    def add_node(self, x, y):
        self.nodes.append(self.new_node(x, y))
        self.node_num += 1

    def new_edge(self, node1, node2):
        edge = node1.new_edge_to(node2, self.edge_color)
        node1.add_neighbor(node2, edge)
        node2.add_neighbor(node1, edge)
        return edge

    def add_edge(self, node1, node2):
        self.edges.append(self.new_edge(node1, node2))
        self.edge_num += 1

    # draw this graph on screen
    def draw_graph(self):
        for node in self.nodes:
            node.draw()
        for edge in self.edges:
            edge.draw()

    # return a random group  of postions of nodes in a large graph
    def large_graph_nodes(self):
        nodes_group1 = [
            (5, 2), (12, 2), (17, 1), (27, 1), (1, 6),
            (5, 5), (9, 5), (16, 6), (19, 3), (22, 6),
            (27, 6), (30, 3), (1, 13), (4, 10), (12, 8),
            (14, 10), (19, 10), (27, 11), (30, 8), (7, 13),
            (11, 13), (15, 14), (23, 14), (30, 14), (22, 11)
        ]

        return nodes_group1

    # return a random group  of edges in a large graph
    def large_graph_edges(self):
        edges1 = [
            (0, 1), (0, 4), (1, 7), (1, 14), (1, 6),
            (5, 6), (2, 3), (2, 8), (7, 8), (8, 9),
            (8, 16), (3, 9), (3, 10), (10, 11), (11, 18),
            (4, 12), (6, 13), (12, 13), (12, 19), (14, 19),
            (19, 20), (15, 20), (6, 14), (14, 15), (15, 16),
            (16, 21), (9, 24), (21, 22), (16, 22), (17, 24),
            (9, 17), (9, 10), (10, 17), (17, 18), (18, 23),
            (22, 23), (17, 23)
        ]
        return edges1

    # generate a large graph
    def generate_large_graph(self):
        # generate all nodes
        nodes_positions = self.large_graph_nodes()
        for x, y in nodes_positions:
            self.add_node(x, y)
        # generate all edges
        nodes_connections = self.large_graph_edges()
        for n1, n2 in nodes_connections:
            self.add_edge(self.nodes[n1], self.nodes[n2])

    # set the start node of graph algorithm
    def set_root(self, node_id):
        self.root = self.nodes[node_id]

    # draw a large graph on the screen
    def draw_large_graph(self):
        self.generate_large_graph()
        self.draw_graph()

    # display graph on panel
    def display_graph(self, times):
        for i in range(times):
            self.screen.frame()

    # update color of a node in this graph
    def update_node_color(self, node, color):
        node_id = node.get_id()
        self.nodes[node_id].change_color(color)

    # update color of a node in this graph
    def update_edge_color(self, edge, color):
        edge.change_color(color)

    # visit the edge
    def visit_edge(self, edge):
        self.update_edge_color(edge, self.visited_edge_color)
        self.draw_graph()
        self.display_graph(self.duration)

    # leave the edge
    def leave_edge(self, edge):
        self.update_edge_color(edge, self.edge_color)
        self.draw_graph()
        self.display_graph(self.duration)

    # visit the node alone
    def visit_node(self, node):
        node.mark_visited()
        self.update_node_color(node, self.visited_node_color)
        self.draw_graph()
        self.display_graph(self.duration)

    # entry for BFS
    def bfs_start(self):
        if (self.root == None):
            self.root = self.nodes[9]
        self.bfs(self.root)

    # BFS Algorithm
    def bfs(self, root):
        queue_node = deque([root, ])
        queue_edge = deque([])

        while queue_node:
            n = len(queue_node)
            for i in range(n):
                node = queue_node.popleft()
                if (queue_edge):
                    edge_from = queue_edge.popleft()
                    self.visit_edge(edge_from)
                self.visit_node(node)
                for neighbor, edge in node.get_edges().items():
                    if not neighbor.visited:
                        queue_node.append(neighbor)
                        queue_edge.append(edge)

    # entry for DFS
    def dfs_start(self):
        if (self.root == None):
            self.root = self.nodes[9]
        self.dfs(self.root)

    # DFS Algorithm
    def dfs(self, node):
        self.visit_node(node)

        for neighbor, edge in node.get_edges().items():
            if not neighbor.visited:
                self.visit_edge(edge)
                self.dfs(neighbor)
                self.leave_edge(edge)
