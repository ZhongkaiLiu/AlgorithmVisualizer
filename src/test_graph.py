from graph_algorithm import GraphAlgorithm

duration = 2
root = 9

print("point graph BFS")
graph1 = GraphAlgorithm("point", duration, root)
graph1.bfs()

print("point graph DFS")
graph2 = GraphAlgorithm("point", duration, root)
graph2.dfs()

print("node graph BFS")
graph1 = GraphAlgorithm("cross", duration, root)
graph1.bfs()

print("node graph DFS")
graph2 = GraphAlgorithm("cross", duration, root)
graph2.dfs()
