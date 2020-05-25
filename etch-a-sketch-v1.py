# REPLACE THIS WITH YOUR NAME

# WORKS CITED:
# emoji list https://unicode.org/emoji/charts/full-emoji-list.html
# REPLACE THIS WITH WEBSITE LINKS OR NAMES OF CLASSMATE HELPERS

# UPGRADES: 
# REPLACE THIS WITH A DESCRIPTION OF YOUR UPGRADE(S)

######### imports

from getkey import getkey, keys
import random

######### constants 

TITLE = "Etch A Sketch"
TITLE_ROW_NUM = 1
TITLE_COL_NUM = 1

INSTRUCTIONS = "Use the arrow keys to draw a sketch."
INSTRUCTIONS_ROW_NUM = 2
INSTRUCTIONS_COL_NUM = 1

INITIAL_STATUS_MESSAGE = "(f)aster s(l)ower (e)xit"
STATUS_ROW_NUM = 3
STATUS_COL_NUM = 1

# colors 
# 0 default, 30 black, 31 red
# 32 green, 33 yellow, 34 blue
# 35 magenta, 36 cyan, 37 white
TEXT_COLOR = 0 

BOARD_ROW_NUM = 4
BOARD_COL_NUM = 5

PLAYER_SYMBOL = "\N{mouse}"
INITIAL_PLAYER_ROW = random.randint(BOARD_ROW_NUM, 10)
INITIAL_PLAYER_COL = random.randint(BOARD_COL_NUM, 10)

######### variables

isGameOver = False
statusMessage = INITIAL_STATUS_MESSAGE

# player position on the board
playerRow = INITIAL_PLAYER_ROW
playerCol = INITIAL_PLAYER_COL

# players speed (# of units per step)
moveAmount = 1  

######### functions 

def displayText(text, row, col):
  # displays text at position row, col

  # position cursor for text
  print("\033[" + str(row) + ";" + str(col) + "H", end = "")

  # clear the current line
  #    0K clears current line to the right of the cursor 
  #    1K clears to the left of the cursor
  #    2K clears the entire line
  print("\033[2K", end = "")

   # set printing color to TEXT_COLOR
  print("\033[" + str(TEXT_COLOR) + "m", end = "");

  # display the desired text
  print(text)

######### main program 

#### initial setup

# hide cursor
print("\033[?25l")

# clear screen and set cursor to top left corner 
# 3J resets screen buffer (may be unnecessary)
print("\033[3J")

displayText(TITLE, TITLE_ROW_NUM, TITLE_COL_NUM)
displayText(INSTRUCTIONS, INSTRUCTIONS_ROW_NUM, INSTRUCTIONS_COL_NUM)
displayText(statusMessage, STATUS_ROW_NUM, STATUS_COL_NUM)

#### main game loop

while not isGameOver:
  # move cursor to location of player
  print("\033[" + str(BOARD_ROW_NUM + playerRow) + ";" + str(BOARD_COL_NUM + playerCol) + "H", end = "")

  # display player symbol
  print(PLAYER_SYMBOL) 

  playerMove = getkey()

  # player moves right
  if playerMove in [keys.RIGHT, "d"]:
    playerCol += moveAmount
  # player moves left
  elif playerMove in [keys.LEFT, "a"]:
    playerCol -= moveAmount
  # player moves down
  elif playerMove in [keys.DOWN, "s"]:
    playerRow += moveAmount
  # player moves up
  elif playerMove in [keys.UP, "w"]:
    playerRow -= moveAmount
  # move player faster
  elif playerMove in ["f"]:
    moveAmount += 1
  # move player slower
  elif playerMove in ["l"]:
    if moveAmount > 1:
      moveAmount -= 1
  # player wants to exit
  elif playerMove in ["e"]:
    statusMessage = "Goodbye"
    displayText(statusMessage, STATUS_ROW_NUM, STATUS_COL_NUM)
    isGameOver = True

# move cursor far down the screen out of the way (may be unnecessary)
print("\033[30;1H")
