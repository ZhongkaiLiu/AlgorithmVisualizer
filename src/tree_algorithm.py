import panel
import tree


class TreeAlgorithm(object):

    def __init__(self):
        self.screen = panel.Panel()
        self.tree = tree.Tree(self.screen)

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
