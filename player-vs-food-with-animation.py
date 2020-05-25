# REPLACE THIS WITH YOUR NAME

# WORKS CITED
# REPLACE THIS WITH WEBSITE LINKS 

# UPGRADES: 
# REPLACE THIS WITH A DESCRIPTION OF YOUR UPGRADE(S)

######### imports

import random
# https://docs.python.org/2/library/curses.html
import curses   
from curses import textpad

######### constants 

TITLE = "Player vs Food"
TITLE_ROW = 1
TITLE_COL = 1

INSTRUCTIONS = "Use the arrow keys to move the player"
INSTRUCTIONS_ROW = 2
INSTRUCTIONS_COL = 1

INITIAL_STATUS_MESSAGE = "Score: 0"
STATUS_ROW = 3
STATUS_COL = 1

# top left corner of board
BOARD_ROW = 4 
BOARD_COL = 1 

# board size
BOARD_WIDTH = 20
BOARD_HEIGHT = 10

PLAYER_SYMBOL = "P"
FOOD_SYMBOL = "F"

# start player in top left corner of board
INITIAL_PLAYER_ROW = BOARD_ROW + 1
INITIAL_PLAYER_COL = BOARD_COL + 1
# TODO - start the player in a random location

######### variables

# screen
screen = curses.initscr()

# allowing the colors red and green to be used with 
# default background (-1)
curses.start_color()
curses.use_default_colors()
# player color is red (pair #1)
curses.init_pair(1, curses.COLOR_RED, -1)
# food color is green (pair #2)
curses.init_pair(2, curses.COLOR_GREEN, -1)
# TODO - learn more about color in Curses programming
# at https://docs.python.org/3/howto/curses.html#attributes-and-color

# game control flag variables
isGameOver = False

# game loop timer
# 1000 = 1 second, 100 = 1 tenth of a second
gameSpeed = 1000

# score
score = 0

playerRow = INITIAL_PLAYER_ROW
playerCol = INITIAL_PLAYER_COL

# initial player direction
playerDirection = "right"
userKeyPress = curses.KEY_RIGHT

# place food next to player
foodRow = playerRow + 1
foodCol = playerCol + 1
# TODO - place the food in a random location

statusMessage = INITIAL_STATUS_MESSAGE

######### functions 

# TODO - Improve this program by making a function

######### main program

#  initial setup

# prevent inputs from showing on screen
curses.noecho() 
curses.curs_set(0)

screen.nodelay(1)
screen.timeout(gameSpeed)

# to use the arrow keys
screen.keypad(True)

keyPressed = curses.KEY_RIGHT

# display text
screen.addstr(TITLE_ROW, TITLE_COL, TITLE)
screen.addstr(INSTRUCTIONS_ROW, INSTRUCTIONS_COL, INSTRUCTIONS)
screen.addstr(STATUS_ROW, STATUS_COL, statusMessage)

# draw the game board
textpad.rectangle(screen, BOARD_ROW, BOARD_COL, BOARD_ROW + BOARD_HEIGHT, BOARD_COL + BOARD_WIDTH)

# place player
screen.addstr(playerRow, playerCol, PLAYER_SYMBOL,curses.color_pair(1)) 

# place food
screen.addstr(foodRow, foodCol, FOOD_SYMBOL, curses.color_pair(2))

# main game loop

while not(isGameOver):
  # user input
  screen.refresh()
  key = screen.getch()
  
  # erase player in previous position
  screen.addstr(playerRow, playerCol, " ")

  if key in [
    ord('a'), ord('d'), ord('s'), ord('w'), ord('q'), 
    curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_UP
  ]:
    keyPressed = key



  # move to the right
  if keyPressed in [ord('d'), curses.KEY_RIGHT]:
    playerDirection = "right"
  # move to the left
  elif keyPressed in [ord('a'), curses.KEY_LEFT]:
    playerDirection = "left"
  # move down
  elif keyPressed in [ord('s'), curses.KEY_DOWN]:
    playerDirection = "down"
  # move up
  elif keyPressed in [ ord('w'), curses.KEY_UP]:
    playerDirection = "up"
  # user wants to quit
  elif keyPressed in [ ord('q')]:
    isGameOver = True

  if playerDirection == "right":
    playerCol += 1
  elif playerDirection == "left":
    playerCol -= 1
  elif playerDirection == "up":
    playerRow -= 1
  elif playerDirection == "down":
    playerRow += 1
    
  # draw player in new position
  screen.addstr(playerRow, playerCol, PLAYER_SYMBOL,curses.color_pair(1))

  # collision detection - player found the food
  if playerRow == foodRow and playerCol == foodCol:
    # score a point
    score += 1
    
    # TODO - Help Mr. Minich fix this
    # place new food somewhere in the board 
    #foodRow = random.randint(?, ?)
    #foodCol = random.randint(?, ?)

    #screen.addstr(?, ?, FOOD_SYMBOL)
    # update the status with the new score
    statusMessage = "Score: " + str(score)
    screen.addstr(STATUS_ROW, STATUS_COL, statusMessage)

  # collision detection - player hit right boundary
  if playerCol <= BOARD_COL:
    # update status
    statusMessage = "Game Over. You hit the left boundary."

    screen.addstr(STATUS_ROW, STATUS_COL, statusMessage)
      
    # TODO - Help Mr. Minich fix this so game ends
    # isGameOver = True

    # TODO - Add boundary detection for all boundaries

  screen.timeout(gameSpeed)
