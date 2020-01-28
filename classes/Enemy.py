import pygame
import copy
import time

class Enemy():
	def __init__(self):
		pass
		
	def renderEnemy(self, enemypos, display):
		enemyImg = pygame.image.load('tiles/Enemy.png')
		for i in enemypos:
			display.blit(enemyImg, (i[0], i[1]))

	def moveEnemy(self, enemyarr, graph, x, y):
		#20x20 level
		# print(x, y)
		print(enemyarr)
		for e in enemyarr:
			self.shpath = [0]*100
			path = []
			print(e[0], e[1], x, y)
			visited = [[0 for i in range(20)] for j in range(20)]
			self.findPath(e[0], e[1], x, y, graph, visited, path)

			print(shpath)



	def findPath(self, a, b, x, y, graph, visited, path):
		path += [[a, b]]
		# print(path)
		time.sleep(0.1)

		if a == x and b == y:
			if len(path)<len(self.shpath):
				self.shpaht = copy.deepcopy(path)
			return

		visited[a][b] = 1
		for elem in graph[(a, b)]:
			if visited[elem[0]][elem[1]] == 0:
				self.findPath(elem[0], elem[1], x, y, graph, visited, path)

		visited[a][b] = 0
		temp = path.pop()


