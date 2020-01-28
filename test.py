from collections import defaultdict
import copy
import time
import queue
shpath = [0]*100

def findPath(a, b, x, y, graph, visited, path):
	global shpath
	path += [[a, b]]
	# print(path)
	# time.sleep(0.1)

	if a == x and b == y:
		if len(path)<len(shpath):
			shpaht = copy.deepcopy(path)
		return

	visited[a][b] = 1
	for elem in graph[(a, b)]:
		if visited[elem[0]][elem[1]] == 0:
			findPath(elem[0], elem[1], x, y, graph, visited, path)

	visited[a][b] = 0
	temp = path.pop()

level =     [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
			 [1, 0, 1, 1, 1, 0, 1, 0, 1, 2,1],
			 [1, 0, 1, 1, 1, 0, 0, 0, 0, 0,1],
			 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0,1],
			 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0,1],
			 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0,1],
			 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0,1],
			 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0,1],
			 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0,1],
			 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0,1],
			 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0,1],
			 [1, 0, 0, 0, 0, 0, 0, 3, 0, 0,1],
			 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1]]

graph = defaultdict(list)
for i in range(1, len(level)-1):
	for j in range(1, len(level[i])-1):
		if level[i][j] != 1 and level[i-1][j] != 1:
			graph[(i, j)] += [(i-1, j)]
		if level[i][j] != 1 and level[i+1][j] != 1:
			graph[(i, j)] += [(i+1, j)]
		if level[i][j] != 1 and level[i][j-1] != 1:
			graph[(i, j)] += [(i, j-1)]
		if level[i][j] != 1 and level[i][j+1] != 1:
			graph[(i, j)] += [(i, j+1)]

print(graph)

path = []
visited = [[0 for i in range(20)] for j in range(20)]
findPath(11, 7, 1, 9, graph, visited, path)