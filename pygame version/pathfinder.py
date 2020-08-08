from heapq import heapify, heappush, heappop
import math
import pygame as pg
import time
import sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (80, 220, 80)
RED = (230, 70, 70)
YELLOW = (255, 255, 50)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
LIGHTBLUE = (64, 224, 208)


# This sets the WIDTH and HEIGHT of the grid canvas
WIDTH = 799
GAP = 1
ROW = 50
WIN = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("A* PathFinder")


#############################################----classes and functions-----##########################################

class Block:
	def __init__(self, row, col, width):
		self.color = WHITE
		self.row = row
		self.col = col
		self.x = col * (width + GAP)
		self.y = row * (width + GAP)
		self.width = width
		self.neighbor = []

	def get_pos(self):
		return self.x, self.y

	def set_start(self):
		self.color = ORANGE

	def set_goal(self):
		self.color = LIGHTBLUE

	def set_closed(self):
		self.color = RED

	def set_opened(self):
		self.color = GREEN

	def set_obs(self):
		self.color = BLACK

	def set_path(self):
		self.color = YELLOW

	def is_start(self):
		return self.color == ORANGE

	def is_goal(self):
		return self.color == LIGHTBLUE

	def is_closed(self):
		return self.color == RED

	def is_opened(self):
		return self.color == GREEN

	def is_obs(self):
		return self.color == BLACK

	def erase(self):
		self.color = WHITE
	

	def draw(self, win):
		pg.draw.rect(win, self.color, (self.x, self.y , self.width, self.width))

	def find_neighbors(self, grid):
		row = self.row
		col = self.col
		if row < ROW - 1 and not grid[row+1][col].is_obs():    # Check DOWN
			self.neighbor.append((row+1, col))
		if col < ROW -1 and not grid[row][col+1].is_obs():     # Check RIGHT
			self.neighbor.append((row, col+1))
		if row > 0 and not grid[row-1][col].is_obs():          # Check UP
			self.neighbor.append((row-1, col))
		if col > 0 and not grid[row][col-1].is_obs():          # Check LEFT
			self.neighbor.append((row, col-1))



def heuristic(pos1, pos2):
	distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
	return distance


def make_grid():
	grid = []
	width = WIDTH // ROW
	for i in range(ROW):
		grid.append([])
		for j in range(ROW):
			grid[i].append(Block(i, j, WIDTH // ROW))
	return grid


def draw_grid(win, grid):
	win.fill(BLACK)
	for rows in grid:
		for blocks in rows:
			blocks.draw(win)
	pg.display.update()


def curr(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	grid[row][col].draw(LIGHTGREEN, win)
	pg.display.update()


def astar(start, goal, grid, draw):
	# Initialize frontier heap list, visited list
	frontierinfo = []
	frontierpoint = {}
	visited = {}
	rank = 0
	
	heappush(frontierinfo, [heuristic(start.get_pos(), goal.get_pos()), 0, rank, start, start])
	frontierpoint[(start.row, start.col)] = 1
	
	# start looping
	while len(frontierinfo):
		for event in pg.event.get():  # User did something
			if event.type == pg.QUIT:
				pg.quit()
		if visited.get((goal.row, goal.col)) != None:  # goal in visited means shortest path is found already
			cur = visited[(goal.row, goal.col)]
			while cur != (start.row, start.col): # this loop to back traverse the optimal path using the dictionary
				grid[cur[0]][cur[1]].set_path()
				cur = visited[cur]
				draw()
			start.set_start()
			goal.set_goal()
			draw()
			break
		expel = heappop(frontierinfo)
		current = expel[-1] # pop out the one with smallest total est cost
		current.set_opened()
		nextstep = current.neighbor # find neighbors
		for item in nextstep:
			if visited.get(item) != None: pass 
			elif item == (current.row, current.col): pass
			elif frontierpoint.get(item) != None: pass
			else:
				rank += 1
				heappush(frontierinfo, [expel[1]+21+heuristic(item, goal.get_pos()),
										expel[1]+21, rank,\
										current, grid[item[0]][item[1]]])
				frontierpoint[item] = 1
				grid[item[0]][item[1]].set_opened()
		
		frontierpoint.pop((current.row, current.col))
		if current != start and current != goal:
			current.set_closed()
		visited[(current.row, current.col)] = (expel[-2].row, expel[-2].col) # store in dictionary the optimal last step

		draw()


##############################################----individual blocks-----##########################################

def main(win):
	run = True
	started = False
	dist = (WIDTH // ROW) + GAP
	grid = make_grid()

	start = None
	goal = None

	while run:
		draw_grid(win, grid)
		for event in pg.event.get():  # User did something
			if event.type == pg.QUIT:  # If user clicked close
				run = False  # Flag that we are done so we exit this loop
			if started:
				continue
			else:
				if pg.mouse.get_pressed()[0]:
					pos = pg.mouse.get_pos()
					col = (pos[0] // dist)
					row = (pos[1] // dist)
					block = grid[row][col]
					if not start and block != goal:
						start = block
						start.set_start()
					elif not goal and block != start:
						goal = block
						goal.set_goal()
					elif block != start and block != goal:
						block.set_obs()
				if pg.key.get_pressed()[pg.K_c]: # hold down "c" key and use mouse to clean board
					if pg.mouse.get_pressed()[0]:
						pos = pg.mouse.get_pos()
						col = (pos[0] // dist)
						row = (pos[1] // dist)
						block = grid[row][col]
						if block == start:
							start = None
						if block == goal:
							goal = None
						block.erase()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE and start and goal: 
						for rows in grid:
							for blocks in rows:
								if not blocks.is_obs() and not blocks.is_start() and not blocks.is_goal():
									blocks.erase()
								blocks.neighbor = []
								blocks.find_neighbors(grid)
						astar(start, goal, grid, lambda: draw_grid(win, grid))
					if event.key == pg.K_r:
						start = None
						goal = None
						grid = make_grid()

	pg.quit()

main(WIN)