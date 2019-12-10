from panel import Panel
from line import Line


class Node(object):
    # bind Node with a screen object
    def __init__(self, x, y, color, screen, nid):
        if (not isinstance(screen, Panel)):
            raise ValueError("screen must be an object of class Panel!")
        else:
            self.id = nid
            self.x = x
            self.y = y
            self.color = color
            self.screen = screen

    # draw a point Node on screen, BUT no refresh, need refresh to display later
    def draw(self):
        # print("when draw node, node {}, color is {}".format(self.id, self.color))
        self.screen.draw_point(self.x, self.y, self.color)

    # draw this Node on screen, AND immediately refresh to display
    def draw_refresh(self):
        self.draw()
        self.screen.refresh()

    def change_color(self, color):
        self.color = color

    # return an instance of class Line that connects two point nodes
    def line_connect_to(self, node, color):
        return Line(self.x, self.y, node.x, node.y, color, self.screen)

    def get_id(self):
        return self.id


# TreeNode inherited from class Node
# TreeNode has parent, children
class TreeNode(Node):
    def __init__(self, x, y, color, screen, nid):
        super().__init__(x, y, color, screen, nid)
        self.parent = None
        self.line = None
        self.left = None
        self.right = None

    def set_children(self, left, right):
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_children(self):
        return (self.left, self.right)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    # For each TreeNode, it has only one line from parent to it
    def set_line(self, line):
        self.line = line

    def get_line(self):
        return self.line

    def isLeaf(self):
        return self.left == None and self.right == None

    def isRoot(self):
        return self.parent == None


class GraphNode(Node):
    def __init__(self, x, y, node_color, edge_color, screen, nid):
        super().__init__(x, y, node_color, screen, nid)
        # self.neighbors = set()
        self.edges = {}
        self.visited = False

    def mark_visited(self):
        self.visited = True

    def new_edge_to(self, node, edge_color):
        return self.line_connect_to(node, edge_color)

    def add_neighbor(self, node, edge):
        # self.neighbors.add(node)
        self.edges[node] = edge

    def get_edges(self):
        return self.edges