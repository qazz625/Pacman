import pygame

class Enemy():
	def __init__(self):
		pass
		
	def renderEnemy(self, enemypos, display):
		enemyImg = pygame.image.load('tiles/Enemy.png')
		for i in enemypos:
			display.blit(enemyImg, (i[0], i[1]))
