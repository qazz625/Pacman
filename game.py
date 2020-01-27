import pygame
import time
from levels import level1
from classes import Player, Map, Enemy

white = (0, 0, 0)
blue = (0, 0, 255)

level = level1.level

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

	pl = Player.Player()
	e = Enemy.Enemy()
	m = Map.Map(level)

	score = 0
	while not dead and not win:
		t = time.time()
		for event in pygame.event.get():
			dead, x_change, y_change = pl.movePlayer(x_change, y_change, event)

		gameDisplay.fill(white)

		m.renderMap(display_width, display_height, gameDisplay, level)

		#check whether position to be moving in is valid
		score, dead, x_change, y_change = m.checkCollision(score, x_change, y_change, x, y, level)

		#move player
		x += x_change
		y += y_change

		pl.renderPlayer(x, y, gameDisplay)
		e.renderEnemy(enemypos, gameDisplay)

		pygame.display.update()
		clock.tick(30)


	pygame.quit()
	quit()


Game()

		






