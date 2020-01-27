import pygame
import time
from levels import level1
# from tiles import 

white = (0, 0, 0)
blue = (0, 0, 255)

'''
-1 = empty
0 = dot
1 = wall
2 = player
3 = enemy
'''


level = level1.level

wallarr = []
dotarr = []
enemyarr = []
for i in range(len(level)):
	for j in range(len(level[i])):
		if level[i][j] == 1:
			wallarr += [pygame.Rect(j*34, i*34, 34, 34)]
		elif level[i][j] == 0:
			dotarr += [[pygame.Rect(j*34+11, i*34+11, 12, 12), i, j]]
		elif level[i][j] == 3:
			enemyarr += [[pygame.Rect(j*34+2, i*34+2, 30, 30), i, j]]



class Player():
	def __init__(self, x, y, display):
		playerImg = pygame.image.load('tiles/player.png')
		display.blit(playerImg, (x, y))


class Map():
	def __init__(self, width, height, display, level):
		#11 X 17
		self.level = level
		dotImg = pygame.image.load('tiles/dot.png')
		for i in range(len(self.level)):
			for j in range(len(self.level[i])):
				if self.level[i][j] == 1:
					pygame.draw.rect(display, blue, (j*34, i*34, 34, 34), 0)
				elif self.level[i][j] == 0:
					display.blit(dotImg, (j*34+11, i*34+11))

class Enemy():
	def __init__(self, enemypos, display):
		enemyImg = pygame.image.load('tiles/Enemy.png')
		for i in enemypos:
			display.blit(enemyImg, (i[0], i[1]))

		


def Game():
	pygame.init()
	display_width = 700
	display_height = 700

	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption('Pacman')
	clock = pygame.time.Clock()

	dead = False
	win = False

	#starting position of the player
	var = 0
	for i in range(len(level)):
		for j in range(len(level[i])):
			if level[i][j] == 2:
				var = 1
				break
		if var == 1:
			break

	x = j*34+2
	y = i*34+2
	x_change = 0
	y_change = 0


	#starting position of the enemy
	enemypos = []
	var = 0
	for i in range(len(level)):
		for j in range(len(level[i])):
			if level[i][j] == 3:
				enemypos += [[i, j]]

	for i in range(len(enemypos)):
		enemypos[i][0], enemypos[i][1] = enemypos[i][1]*34 + 2, enemypos[i][0]*34 + 2





	score = 0
	while not dead and not win:
		t = time.time()
		for event in pygame.event.get():
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


		gameDisplay.fill(white)
		m = Map(display_width, display_height, gameDisplay, level)

		p = pygame.Rect(x+x_change, y+y_change, 30, 30)

		#checking collision with walls
		for lol in wallarr:
			if p.colliderect(lol):
				x_change = 0
				y_change = 0

		#checking collision with dots
		for lol in dotarr:
			if p.colliderect(lol[0]):
				level[lol[1]][lol[2]] = -1
				score += 1

		#checking collision with enemies
		for lol in enemyarr:
			if p.colliderect(lol[0]):
				dead = True
				break


		x += x_change
		y += y_change

		
		p = Player(x, y, gameDisplay)
		e = Enemy(enemypos, gameDisplay)
		pygame.display.update()
		clock.tick(20)


	pygame.quit()
	quit()


Game()

		






