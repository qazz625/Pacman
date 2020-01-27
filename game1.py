import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

carImg = pygame.image.load('player.png')

def car(x, y):
	gameDisplay.blit(carImg, (x, y))

x = display_width*0.45
y = display_height*0.7

x_change = 0
y_change = 0


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('A game')

clock = pygame.time.Clock()

crashed = False

while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change -= 2
			elif event.key == pygame.K_RIGHT:
				x_change += 2
			elif event.key == pygame.K_UP:
				y_change -= 2
			elif event.key == pygame.K_DOWN:
				y_change += 2

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_change = 0


		# print(event)
	x += x_change
	y += y_change
	gameDisplay.fill(white)
	car(x, y)
	pygame.display.update()
	clock.tick(40)

pygame.quit()
quit()