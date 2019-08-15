import random 

import pygame, sys

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

pygame.font.init()
shape_colors = [
	(0, 0, 0),
	(0, 120, 10),
	(30, 73, 120),
	(40, 49, 230),
	(230, 120, 40),
	(120, 90, 30),
	(0, 110, 70)
]

class Piece(object):
	cols = 10 #x
	rows = 20 #y

	def __init__(self, col, row, shape):
		self.x = col
		self.y = row
		self.shape = shape
		self.color = shape_colors[shapes.index(shape)]
		self.rotation = 0

def main():
	global grid
	locked_positions = {}
	grid = create_grid(locked_positions)

	change_piece = False
	run = True
	current_piece = get_shape()
	next_piece = get_shape()
	clock = pygame.time.Clock()
	fall_time = 0

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.display.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					current_piece.x -=1
					if not valid_space(current_piece, grid):
						current_piece.x +=1

				elif event.key == pygame.K_RIGHT:
					current_piece.x +=1
					if not valid_space(current_piece, grid):
						current_piece.x -=1

				elif event.key == pygame.K_UP:
					current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
					if not valid_space(current_piece, grid):
						current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
			if event.type == pygame.K_DOWN:
				current_piece.y += 1
				if not valid_space(current_piece, grid):
					current_piece.y -=1


		draw_window(window)

def draw_window(surface):
	pass

def create_grid(locked_positions = {}):
	grid = [[(0,0,0) for x in range(10)] for x in range(20)]

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (j,i) in locked_positions:
				c = locked_positions[(j,i)]
				grid[i][j] = c

	return grid
def draw_grid(surface, row, col):
	pass
def valid_space(shape, grid):
    pass
def get_shape():
	global shapes, shape_colors
	return Piece(5, 0, random.choice(shapes))
window = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

grid = create_grid()
window.fill((0,0,0))

font = pygame.font.SysFont('comicsans', 60)
label = font.render('TETRIS', 1, (255, 255, 255))

window.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

for i in range(len(grid)):
	for j in range(len(grid[i])):
		pygame.draw.rect(window, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)

draw_grid(window, 20, 10)
pygame.draw.rect(window, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
pygame.display.update()




main()