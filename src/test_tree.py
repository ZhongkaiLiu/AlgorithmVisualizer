from tree_algorithm import TreeAlgorithm

duration = 1

tree1 = TreeAlgorithm("point", duration)
print("point tree inorder")
tree1.inorder()

tree2 = TreeAlgorithm("point", duration)
print("point tree preorder()")
tree2.preorder()

tree3 = TreeAlgorithm("point", duration)
print("point tree postorder")
tree3.postorder()

tree4 = TreeAlgorithm("point", duration)
print("point tree levelorder")
tree4.levelorder()

tree5 = TreeAlgorithm("cross", duration)
print("cross tree inorder")
tree5.inorder()

tree6 = TreeAlgorithm("cross", duration)
print("cross tree preorder()")
tree6.preorder()

tree7 = TreeAlgorithm("cross", duration)
print("cross tree postorder")
tree7.postorder()

tree8 = TreeAlgorithm("cross", duration)
print("cross tree levelorder")
tree8.levelorder()
