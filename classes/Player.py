import pygame

class Player():
	def __init__(self):
		pass

	def renderPlayer(self, x, y, display):
		playerImg = pygame.image.load('tiles/player.png')
		display.blit(playerImg, (x, y))

	def movePlayer(self, x_change, y_change, event):
		dead = False
		if event.type == pygame.QUIT:
			dead = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change -= 34
			elif event.key == pygame.K_RIGHT:
				x_change += 34
			elif event.key == pygame.K_UP:
				y_change -= 34
			elif event.key == pygame.K_DOWN:
				y_change += 34

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_change = 0

		return dead, x_change, y_change