import numpy as np
from spark.model.BFS import BFS
from spark.HexGui import HexGui

# adjNodes
test_22 = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
assert sorted(BFS.adjNodes((2, 2), 8)) == sorted(test_22), BFS.adjNodes((2, 2), 8)
test_11 = [(1, 2), (2, 1)]
assert sorted(BFS.adjNodes((1, 1), 8)) == sorted(test_11), BFS.adjNodes((1, 1), 8)

# bfs
state = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0,2], [0,0,0,0,0,0,1,0,0], [0,0,0,0,0,2,1,1,1], [0,2,1,2,1,1,2,2,2], [0,2,2,2,2,1,2,1,0], [0,1,1,2,1,2,1,0,0], [0,0,0,2,2,1,0,0,0], [0,1,0,2,1,0,0,0,0]]
assert BFS.bfs(state) == 2, BFS.bfs(state)
state = [[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,2,1,0],[0,0,1,2,1,0,0],[0,1,2,2,1,0,1],[0,2,1,2,2,2,0],[0,0,1,2,1,0,0]]
assert BFS.bfs(state) == None, BFS.bfs(state)
state = [[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,2,1,0],[0,0,1,2,1,0,0],[0,1,2,2,1,0,1],[0,2,1,2,2,2,2],[0,0,1,2,1,0,0]]
assert BFS.bfs(state) == 2, BFS.bfs(state)