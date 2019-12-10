import random
from panel import Panel
from node_point import TreeNode
from collections import deque


class Tree(object):
    def __init__(self, screen):
        if (not isinstance(screen, Panel)):
            raise ValueError("screen must be an object of class Panel!")
        else:
            self.screen = screen
            self.nodes = []
            self.lines = []
            self.node_num = 0
            self.line_num = 0
            self.root = None
            self.duration = 1
            # set node_color to WHITE as default
            self.node_color = 3
            # set line_color to GREEN as default
            self.line_color = 7
            # set visited node color to RED as default
            self.visited_node_color = 1
            # set visited line color to GREEN as default
            self.visited_line_color = 2

    # set node and line color of this tree
    # avoid setting color after having nodes or lines
    def set_color(self, node_color, line_color, visited_node_color, visited_line_color):
        self.node_color = node_color
        self.line_color = line_color
        self.visited_node_color = visited_node_color
        self.visited_line_color = visited_line_color

    # set duration
    def set_duration(self, duration):
        self.duration = duration

    # return a new node at (x, y)
    def new_node(self, x, y):
        return TreeNode(x, y, self.node_color, self.screen, self.node_num)

    # return the line that connects two existing node in this tree with line
    # node1 should be parent node
    # node2 should be children node
    def new_connection(self, node1, node2):
        line = node1.line_connect_to(node2, self.line_color)
        if (node2.x < node1.x):
            node1.set_left(node2)
        else:
            node1.set_right(node2)
        node2.set_parent(node1)
        node2.set_line(line)
        return line

    # add new node instance to nodes
    def add_node(self, x, y):
        self.nodes.append(self.new_node(x, y))
        self.node_num += 1

    # add new line instance to lines
    def add_line(self, node1, node2):
        self.lines.append(self.new_connection(node1, node2))
        self.line_num += 1

    # draw this tree on screen
    def draw_tree(self):
        for node in self.nodes:
            node.draw()
        for line in self.lines:
            line.draw()

    # return a random group of positions of nodes in a large tree
    def large_tree_nodes(self):
        nodes_group = [(15, 1), (12, 4), (18, 4), (9, 7), (15, 7), (21, 7), (6, 10), (
            12, 10), (18, 10), (24, 10), (3, 13), (9, 13), (15, 13), (21, 13), (27, 13)]

        delta = [(0, 0), (1, 0), (2, 0), (3, 0), (-1, 0), (-2, 0),
                 (0, 1), (1, 1), (2, 1), (3, 1), (-1, 1), (-2, 1)]

        i = random.randint(0, len(delta) - 1)
        print("use nodes group {}".format(i))
        dx, dy = delta[i]
        for i in range(0, len(nodes_group)):
            x, y = nodes_group[i]
            nodes_group[i] = (x + dx, y + dy)
        return nodes_group

    # connect a group of nodes in a large tree
    def connect_large_tree(self):
        lines = []
        lines1 = [(0, 1), (0, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
                  (4, 8), (5, 9), (6, 10), (7, 11), (8, 12), (8, 13), (9, 14)]
        lines2 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6), (4, 7),
                  (4, 8), (5, 9), (6, 10), (7, 11), (8, 12), (8, 13), (9, 14)]
        lines3 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6), (4, 7),
                  (4, 8), (5, 9), (6, 10), (7, 11), (7, 12), (9, 13), (9, 14)]
        lines4 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6), (4, 7),
                  (5, 8), (5, 9), (6, 10), (6, 11), (7, 12), (9, 13), (9, 14)]
        lines5 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6), (3, 7),
                  (5, 8), (5, 9), (6, 10), (6, 11), (8, 12), (9, 13), (9, 14)]
        lines6 = [(0, 1), (0, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7),
                  (5, 8), (5, 9), (6, 10), (6, 11), (7, 12), (8, 13), (9, 14)]
        lines.append(lines1)
        lines.append(lines2)
        lines.append(lines3)
        lines.append(lines4)
        lines.append(lines5)
        lines.append(lines6)
        i = random.randint(0, 5)
        print("use line {}".format(i))
        for n1, n2 in lines[i]:
            self.add_line(self.nodes[n1], self.nodes[n2])

    # generate a large tree
    def generate_large_tree(self):
        # generate 15 TreeNodes
        nodes_position = self.large_tree_nodes()
        for x, y in nodes_position:
            self.add_node(x, y)
        # set the first node as the root node of this tree
        self.root = self.nodes[0]
        # generate 14 lines
        self.connect_large_tree()

    # draw a large tree on screen
    def draw_large_tree(self):
        # print("call draw_large_tree()")
        self.generate_large_tree()
        self.draw_tree()

    # display tree on panel
    def display_tree(self, times):
        for i in range(times):
            self.screen.frame()

    # update color of a node in this tree
    def update_node_color(self, node_id, color):
        # print("before change, color is {}".format(self.nodes[node_id].color))
        self.nodes[node_id].change_color(color)
        # print("after change, color is {}".format(self.nodes[node_id].color))

    # update color of a line of a node in this tree
    def update_line_color(self, node_id, color):
        self.nodes[node_id].get_line().change_color(color)

    # visit the line of this node
    def visit_line(self, node):
        node_id = node.get_id()
        self.update_line_color(node_id, self.visited_line_color)
        self.draw_tree()
        self.display_tree(self.duration)

    # leave the line of this node
    def leave_line(self, node):
        node_id = node.get_id()
        self.update_line_color(node_id, self.line_color)
        self.draw_tree()
        self.display_tree(self.duration)

    # visit the node alone
    def visit_node(self, node):
        # print("visit node {}".format(node.get_id()))
        node_id = node.get_id()
        # print("visit node {}, want to change to color {}".format(
        #     node_id, self.visited_node_color))
        self.update_node_color(node_id, self.visited_node_color)
        self.draw_tree()
        self.display_tree(self.duration)

    # entry for inorder traversal
    def inorder_traversal(self):
        self.inorder_recursion(self.root)

    # recursive function for inorder traversal
    def inorder_recursion(self, node):
        # visit left child first
        left = node.get_left()
        if (left != None):
            self.visit_line(left)
            self.inorder_recursion(left)
        # visit this node then
        self.visit_node(node)
        right = node.get_right()
        # visit right child last
        if (right != None):
            self.visit_line(right)
            self.inorder_recursion(right)
        # after visiting this subtree, leave this line
        if (not node.isRoot()):
            self.leave_line(node)

    # entry for preorder traversal
    def preorder_traversal(self):
        self.preorder_recursion(self.root)

    # recursive function for preorder traversal
    def preorder_recursion(self, node):
        # visit this node first
        self.visit_node(node)
        # visit left child then
        left = node.get_left()
        if (left != None):
            self.visit_line(left)
            self.preorder_recursion(left)
        right = node.get_right()
        # visit right child last
        if (right != None):
            self.visit_line(right)
            self.preorder_recursion(right)
        # after visiting this subtree, leave this line
        if (not node.isRoot()):
            self.leave_line(node)

    # entry for postorder traversal
    def postorder_traversal(self):
        self.postorder_recursion(self.root)

    # recursive function for preorder traversal
    def postorder_recursion(self, node):
        # visit left child fist
        left = node.get_left()
        if left:
            self.visit_line(left)
            self.postorder_recursion(left)
        right = node.get_right()
        # visit right child then
        if right:
            self.visit_line(right)
            self.postorder_recursion(right)
        # visit this node last
        self.visit_node(node)
        # after visiting this subtree, leave this line
        if (not node.isRoot()):
            self.leave_line(node)

    def levelorder_traversal(self):
        queue = deque([self.root, ])

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if (not node.isRoot()):
                    self.visit_line(node)
                self.visit_node(node)
                left = node.get_left()
                right = node.get_right()
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
