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

INSTRUCTIONS = "Use the arrow keys to draw a sketch.\n(r)ed w(h)ite (b)lue (e)xit\n(c)lear screen\nany other key to change fill pattern\nspace as eraser"
INSTRUCTIONS_ROW_NUM = 3
INSTRUCTIONS_COL_NUM = 1

INITIAL_STATUS_MESSAGE = ""
STATUS_ROW_NUM = 9
STATUS_COL_NUM = 1

TEXT_COLOR = 0 # default white

BOARD_ROW_NUM = 10
BOARD_COL_NUM = 3

PLAYER_SYMBOL = "\N{pencil}"
# start player in top left corner of board
INITIAL_PLAYER_ROW = 5
INITIAL_PLAYER_COL = 10

######### variables

isGameOver = False
statusMessage = INITIAL_STATUS_MESSAGE

# player position on the board
playerRow = INITIAL_PLAYER_ROW
playerCol = INITIAL_PLAYER_COL
newPlayerRow = INITIAL_PLAYER_ROW
newPlayerCol = INITIAL_PLAYER_COL

# player's speed (# of units per step)
moveAmount = 1  
color = 0
fillSymbol = "*"

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
  displayText(statusMessage, STATUS_ROW_NUM, STATUS_COL_NUM)
  print("\033[" + str(color) + "m", end = "");

  # move cursor to location of player
  print("\033[" + str(BOARD_ROW_NUM + playerRow) + ";" + str(BOARD_COL_NUM + playerCol) + "H", end = "")
  # display fill symbol in this soon-to-be previous location of player
  print(fillSymbol) 

  # update player's position based on last move
  playerRow = newPlayerRow
  playerCol = newPlayerCol

  # move cursor to new location of player
  print("\033[" + str(BOARD_ROW_NUM + playerRow) + ";" + str(BOARD_COL_NUM + playerCol) + "H", end = "")

  # display player symbol in the new location
  print(PLAYER_SYMBOL) 

  # get player's inputted keypress
  userInput = getkey()

  # player moves right
  if userInput in [keys.RIGHT, "d"]:
    newPlayerCol += moveAmount
  
  # player moves left
  elif userInput in [keys.LEFT, "a"]:
    # detect the left board boundary
    if playerCol - moveAmount >= BOARD_COL_NUM:
      newPlayerCol -= moveAmount
  
  # player moves down
  elif userInput in [keys.DOWN, "s"]:
    newPlayerRow += moveAmount
  
  # player moves up
  elif userInput in [keys.UP, "w"]:
    # detect the top board boundary
    if playerRow - moveAmount >= 0:
      newPlayerRow -= moveAmount
  
  # change color to red (31)
  elif userInput in ["r"]:
    color = 31

  # change color to white (37)
  elif userInput in ["h"]:
    color = 37
  
  # change color to blue (34)
  elif userInput in ["b"]:
    color = 34
 
  # clear board
  elif userInput in ["c"]:
    # set cursor to top of board
    print("\033[" + str(BOARD_ROW_NUM) + ";" + str(BOARD_COL_NUM) + "H", end = "")
    # clear rest of console below the point of cursor
    print("\033[0J", end = "")

  # player wants to exit
  elif userInput in ["e"]:
    statusMessage = "Goodbye"
    displayText(statusMessage, STATUS_ROW_NUM, STATUS_COL_NUM)
    isGameOver = True

  # player changes fill symbol
  else:
    fillSymbol = userInput

# move cursor far down the screen out of the way (may be unnecessary)
print("\033[30;1H")
