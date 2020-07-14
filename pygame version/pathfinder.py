from heapq import heapify, heappush, heappop
import math
import pygame as pg
import time
import sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
RED = (255, 0, 0)
YELLOW = (249, 255, 51)
LIGHTGREEN = (0, 255, 0)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 1


#############################################----classes and functions-----##########################################

class block():
	def __init__(self, row, column, width, height, margin):
		self.color = WHITE
		self.obs = False
		self.x = column*(width + margin) + int(width/2) + margin
		self.y = row*(height + margin) + int(height/2) + margin
		self.width = width
		self.height = height
		self.neighbor = []
		self.number = None


	def draw(self, color, win):
		pg.draw.rect(win, color, (self.x - int(self.width/2), self.y - int(self.height/2), self.width, self.height), 0)



class button():
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self, screen):
		pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

		if len(self.text):
			font = pg.font.SysFont('arial', 35)
			text = font.render(self.text, 1, BLACK)
			screen.blit(text, (self.x + (int(self.width / 2) - int(text.get_width() / 2)), \
							   self.y + (int(self.height / 2) - int(text.get_height() / 2))))

	def isOver(self, pos):
		if self.x <= pos[0] <= self.x + self.width:
			if self.y <= pos[1] <= self.y + self.height:
				return True

		return False



def heuristic(num1, num2, grid):
	h = len(grid[0])
	row1 = num1 // h
	col1 = num1 % h
	row2 = num2 // h
	col2 = num2 % h
	# x = grid[row1][col1].x - grid[row2][col2].x
	# y = grid[row1][col1].y - grid[row2][col2].y

	# distance = math.sqrt(x**2 + y**2)
	distance = abs(row1-row2)*(HEIGHT + MARGIN) + abs(col1-col2)*(WIDTH + MARGIN)

	return distance


def neighbor(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	lis = []
	if row > 0 and grid[row-1][col].obs == False:
		lis.append(grid[row-1][col].number)
	if row < (len(grid)-1) and grid[row+1][col].obs == False:
		lis.append(grid[row+1][col].number)
	if col > 0 and grid[row][col-1].obs == False:
		lis.append(grid[row][col-1].number)
	if col < (h-1) and grid[row][col+1].obs == False:
		lis.append(grid[row][col+1].number)
	return lis

def curr(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	grid[row][col].draw(LIGHTGREEN, win)
	pg.display.update()


def new(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	grid[row][col].draw(GREEN, win)
	pg.display.update()


def old(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	grid[row][col].draw(RED, win)
	pg.display.update()


def path(number, grid):
	h = len(grid[0])
	row = number // h
	col = number % h
	grid[row][col].draw(YELLOW, win)
	pg.display.update()


def astar(start, goal, grid):
	w, h = pg.display.get_surface().get_size()
	wait = 1
	if goal.number == start.number:
		return [goal.number]

	# Initialize frontier heap list, visited list
	frontierinfo = []
	frontierpoint = []
	visited = {}
	route = []
	
	heappush(frontierinfo, [heuristic(start.number, goal.number, grid), w*h, 0, start.number, start.number])
	frontierpoint.append(start.number)
	
	# start looping
	while len(frontierinfo):
		# pg.time.delay(wait)
		if goal.number in visited: # goal in visited means shortest path is found already
			cur = goal.number
			route = [goal.number]
			while cur != start.number: # this loop to back traverse the optimal path using the dictionary
				route = [visited[cur]] + route
				path(visited[cur], grid)
				cur = visited[cur]
			break
		current = heappop(frontierinfo) # pop out the one with smallest total est cost
		curr(current[-1], grid)
		nextstep = neighbor(current[-1], grid) # find neighbors
		for item in nextstep:
			if item in visited: pass 
			elif item == current[-1]: pass
			elif item in frontierpoint: pass
				# for info in frontierinfo:
					# if info[-1] == item: 
						# if current[1]+heuristic(current[-1], item, grid) < info[1]: # then need to update the optimal cost
						# 	info[1] = current[1]+heuristic(current[-1], item, grid)
						# 	info[0] = current[1]+heuristic(current[-1], item, grid)+heuristic(item, goal.number, grid)
						# 	info[2] = current[-1]
			else:
				heappush(frontierinfo, [current[2]+heuristic(current[-1], item, grid)+heuristic(item, goal.number, grid),\
										w*h-(current[2]+heuristic(current[-1], item, grid)), current[2]+heuristic(current[-1],\
											item, grid), current[-1], item])
				# heappush(frontierinfo, [current[1]+heuristic(current[-1], item, grid)+heuristic(item, goal.number, grid),\
				# 						current[1]+heuristic(current[-1], item, grid), current[-1], item])
				frontierpoint.append(item)
				new(item, grid)
		
		frontierpoint.remove(current[-1])
		if current[-1] != start.number and current[-1] != goal.number:
			old(current[-1], grid)
		visited[current[-1]] = current[-2] # store in dictionary the optimal last step
	
	# print("shortest path called")
	# for item in route:
	# 	print((item//50, item%50))

	# if route == []:
	# 	print('no solution found!')
	# else:
	# 	return route


def trial(num):
	for i in range(num):
		grid[i][i].draw(BLACK, win)
		pg.display.update()
		pg.time.delay(50)

##############################################----indivual blocks-----##########################################

grid = []

for row in range(30):
	grid.append([])
	for col in range(50):
		grid[row].append(0)

count = 0

for row in range(len(grid)):
	for col in range(len(grid[0])):
		grid[row][col] = block(row, col, WIDTH, HEIGHT, MARGIN)
		grid[row][col].number = count
		count += 1


pg.init()

# Set the HEIGHT and WIDTH of the screen
screen_x = 1200
screen_y = 631

WINDOW_SIZE = [screen_x, screen_y]
win = pg.display.set_mode(WINDOW_SIZE)
# Set the screen background
win.fill(BLACK)

# Set title of screen
pg.display.set_caption("PathFinder")

start = button((128, 255, 0), 1080, 95, 100, 80, 'Start')

goal = button((255, 178, 102), 1080, 275, 100, 80, 'Goal')

wall = button((160, 160, 160), 1080, 450, 100, 80, 'Wall')

start.draw(win)
goal.draw(win)
wall.draw(win)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pg.time.Clock()
# -------- Main Program Loop -----------
status = 0


while not done:
	for event in pg.event.get():  # User did something
		if event.type == pg.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
		else:
			for row in range(30):
				for column in range(50):
					# pg.draw.rect(win, WHITE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
					if grid[row][column].obs == True:
						grid[row][column].draw(BLACK, win)
					else:
						grid[row][column].draw(WHITE, win)

			pg.display.update()
			pg.time.delay(50)
			start = grid[10][5]
			goal = grid[20][40]
			start.draw(BLACK, win)
			goal.draw(BLACK, win)
			for i in range(27):
				grid[i][10].obs = True
				grid[29-i][30].obs = True
				grid[i][10].draw(BLACK, win)
				grid[29-i][30].draw(BLACK, win)
				pg.display.update()
			astar(start, goal, grid)
			pg.time.delay(30000)
			# trial(10)


	# clock.tick(1000)

	# Go ahead and update the screen with what we've drawn.
	pg.display.update()
	time.sleep(0.05)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pg.quit()














