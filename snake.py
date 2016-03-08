import pygame
import random
import time

#necessary pygame initializing
pygame.init()

#define screen size
SCREEN_SIZE = 600

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

SNAKE_SIZE = 15;

actionList = []

direction = [[0, SNAKE_SIZE], [SNAKE_SIZE, 0], [0, -SNAKE_SIZE], [-SNAKE_SIZE, 0]]

head_direction = 1
inst_head_dir = 1

clock = pygame.time.Clock()

#snake initialization
snake = [[260, 300], [285, 300], [300, 300]]

#random seed
random.seed()

done = False
lose = False

#score
score = 0;

BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURP = (135, 0, 255)

#summon initial apple
apple_pos = [int(random.randint(0, 600 - SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE, int(random.randint(0, 600 - SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE]

#summon borders
pygame.mixer.music.load('bb-game.mid')
pygame.mixer.music.play(-1, 0)

#This function creates a new apple position.
#it also assures that the new apple position cannot be inside the snake.
def createNewApple():
	global apple_pos
	apple_pos = [int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE, int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE]
	while (apple_pos in snake):
		apple_pos = [int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE, int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE]




while not done:
	#white background
	screen.fill(WHITE)

	#head def
	head = snake[len(snake) - 1]

	#draw snake
	for x in snake:
		pygame.draw.rect(screen, BLACK, (x[0], x[1], SNAKE_SIZE, SNAKE_SIZE))

	#score text
	font = pygame.font.Font(None, 36)
	score_txt = font.render("Score: " + str(score), 1, (10, 10, 10))
	screen.blit(score_txt, (260, 36))

	#draw apple
	pygame.draw.rect(screen, BLACK, (apple_pos[0], apple_pos[1], SNAKE_SIZE, SNAKE_SIZE))

	

	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop	
		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_UP and not inst_head_dir == 0):
				#head_direction = 2
				inst_head_dir = 2
				actionList.append(2)
				#head[0] = int((head[0] / SNAKE_SIZE)) * SNAKE_SIZE
			elif (event.key == pygame.K_RIGHT and not inst_head_dir == 3):
				#head_direction = 1
				inst_head_dir = 1
				actionList.append(1)
				#head[1] = int((head[1] / SNAKE_SIZE)) * SNAKE_SIZE
			elif (event.key == pygame.K_DOWN and not inst_head_dir == 2):
				#head_direction = 0
				inst_head_dir = 0
				actionList.append(0)
				#head[0] = int((head[0] / SNAKE_SIZE)) * SNAKE_SIZE
			elif (event.key == pygame.K_LEFT and not inst_head_dir == 1):
				#head_direction = 3
				inst_head_dir = 3
				actionList.append(3)
				#head[1] = int((head[1] / SNAKE_SIZE)) * SNAKE_SIZE

	#update direction
	if (len(actionList) != 0):
		head_direction = actionList.pop(0)


	#check for eating apples
	if (head[0] == apple_pos[0] and head[1] == apple_pos[1]):
		snake.append([head[0] + direction[head_direction][0], head[1] + direction[head_direction][1]])
		head = snake[len(snake) - 1]
		score += 1
		#new apple position
		#apple_pos = [int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE, int(random.randint(SNAKE_SIZE, 600 - 2 * SNAKE_SIZE)/SNAKE_SIZE)*SNAKE_SIZE]
		createNewApple()

	#check for losing
	for l in range(0, len(snake) - 2):
		if (head[0] == snake[l][0] and head[1] == snake[l][1]):
			lose = True
			score = 0

	#check for hit border
	if (head[0] == 0 or head[0] == (SCREEN_SIZE - SNAKE_SIZE) or head[1] == 0 or head[1] == (SCREEN_SIZE - SNAKE_SIZE)):
		lose = True;
		score = 0

	if lose == True:
		#while (len(snake) > 3):
			#snake.pop()
		lose = False;
		snake = [[260, 300], [285, 300], [300, 300]]
		head = snake[len(snake) - 1]
		head_direction = 1


	#draw borders
	pygame.draw.line(screen, PURP, (0, 0), (600, 0), 30)
	pygame.draw.line(screen, PURP, (0, 0), (0, 600), 30)
	pygame.draw.line(screen, PURP, (0, 600), (600, 600), 32)
	pygame.draw.line(screen, PURP, (600, 600), (600, 0), 32)

	##move snake##
	snake.pop(0)
	#snake.append([head[0] + direction[head_direction][0], head[1] + direction[head_direction][1]])
	snake.append([int((head[0] / SNAKE_SIZE)) * SNAKE_SIZE + direction[head_direction][0], int((head[1] / SNAKE_SIZE)) * SNAKE_SIZE + direction[head_direction][1]])

	print ("Head position: [" + str(head[0]) + ", " + str(head[1]) + "]")

	pygame.display.flip()

	clock.tick(15)


pygame.quit()




