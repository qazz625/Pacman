import pygame

class Map():
	#Character arrays are created when map is constructed	
	def __init__(self, level):
		#11 X 17
		self.level = level
		self.wallarr = []
		self.dotarr = []
		self.enemyarr = []
		for i in range(len(self.level)):
			for j in range(len(self.level[i])):
				if level[i][j] == 1:
					self.wallarr += [pygame.Rect(j*34, i*34, 34, 34)]
				elif level[i][j] == 0:
					self.dotarr += [[pygame.Rect(j*34+11, i*34+11, 12, 12), i, j]]
				elif level[i][j] == 3:
					self.enemyarr += [[pygame.Rect(j*34+2, i*34+2, 30, 30), i, j]]

	def renderMap(self, width, height, display, level):
		white = (0, 0, 0)
		blue = (0, 0, 255)
		dotImg = pygame.image.load('tiles/dot.png')
		for i in range(len(self.level)):
			for j in range(len(self.level[i])):
				if self.level[i][j] == 1:
					pygame.draw.rect(display, blue, (j*34, i*34, 34, 34), 0)
				elif self.level[i][j] == 0:
					display.blit(dotImg, (j*34+11, i*34+11))

	def checkCollision(self, score, x_change, y_change, x, y, level):
		dead = False
		p = pygame.Rect(x+x_change, y+y_change, 30, 30)

		#checking collision with walls
		for elem in self.wallarr:
			if p.colliderect(elem):
				x_change = 0
				y_change = 0

		#checking collision with dots
		for elem in self.dotarr:
			if p.colliderect(elem[0]):
				level[elem[1]][elem[2]] = -1
				score += 1

		#checking collision with enemies
		for elem in self.enemyarr:
			if p.colliderect(elem[0]):
				dead = True
				break

		return score, dead, x_change, y_change

