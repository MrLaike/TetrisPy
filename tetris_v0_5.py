import pygame
import random

import const

class Main():
	run = True
	def __init__(self, win):
		while self.run:
			win.fill((123, 31, 32))
			pygame.display.update()

			##EXIT 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()


	#def run(self):
		



class Element():
	def __init__(self, x, y, rotate):
		self.x = x
		self.y = x		
		self.rotate = rotate



class Draw():  ##Отвечает за отрисовку всех элементов в окне
	def render():
		pass


class Grid():
	pass


win = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption('Tetris')

main = Main(win)




