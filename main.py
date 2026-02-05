import pygame, sys

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris Overwhelmed")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()