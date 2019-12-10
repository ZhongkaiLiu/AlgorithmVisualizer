from panel import Panel
import tree_cross
import tree_point


class TreeAlgorithm(object):

    def __init__(self, node_shape, duration):
        self.screen = Panel()
        if (node_shape == "cross"):
            self.tree = tree_cross.Tree(self.screen)
        else:
            self.tree = tree_point.Tree(self.screen)
        self.tree.set_duration(duration)

    # display the initial tree on the panel
    def display_init(self):
        self.tree.draw_large_tree()
        self.tree.display_tree(2)

    def inorder(self):
        self.display_init()
        self.tree.inorder_traversal()
        self.tree.display_tree(2)
        self.screen.clean_gpio()

    def preorder(self):
        self.display_init()
        self.tree.preorder_traversal()
        self.tree.display_tree(2)
        self.screen.clean_gpio()

    def postorder(self):
        self.display_init()
        self.tree.postorder_traversal()
        self.tree.display_tree(2)
        self.screen.clean_gpio()

    def levelorder(self):
        self.display_init()
        self.tree.levelorder_traversal()
        self.tree.display_tree(2)
        self.screen.clean_gpio()
