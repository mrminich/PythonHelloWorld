# REPLACE THIS WITH YOUR NAME

# WORKS CITED:
# REPLACE THIS WITH WEBSITE LINKS OR NAMES OF CLASSMATE HELPERS

# UPGRADES: 
# REPLACE THIS WITH A DESCRIPTION OF YOUR UPGRADE(S)

######### imports

from getkey import getkey, keys # for getkey & use arrow keys
import random

######### constants 

TITLE = "Save the COVID-19 Patient"
INSTRUCTIONS = "Save the patient avoid the bomb including the hidden one(s)!"

# height (# of rows)
ROWS = 10

# width (# of columns)          
COLUMNS = 10  

# num of lines from top of screen for the title
VERTICAL_OFFSET_TITLE = 1 

# num of lines from top of screen for the instructions
VERTICAL_OFFSET_INSTRUCTIONS = 2

# num of lines from top of screen for the board    
VERTICAL_OFFSET_BOARD = 5   

# num of lines from top of screen for the status panel
VERTICAL_OFFSET_STATUS_PANEL = VERTICAL_OFFSET_BOARD + ROWS 

# num of moves player has to complete the BOARD w/o losing
MOVES_ALLOWED = 200

PLAYER_START_ROW = int (ROWS / 2)     # row # of player's starting position
PLAYER_START_COL = int (COLUMNS / 2)  # column # of player's starting position

# portal a row must be the same as portal b row
PORTAL1A_ROW = 3
PORTAL1A_COL = 0
PORTAL1B_ROW = PORTAL1A_ROW
PORTAL1B_COL = COLUMNS - 1

# 2 characters must be used for the following symbols
# if necessary, add a space such as "* " rather than just "*"

# fill character for empty positions
F = "  "               

# player's symbol
P = "\N{ambulance} "                         

# bomb symbol
M = "\N{bomb} "    

# hidden bomb symbol
H = "\033[0;30m" + ". " + "\033[0m"  

# symbol for border
B = "\033[0;36;46m" + "B " + "\033[0m"                              

# symbol for the patient
E = "\N{face with medical mask} "     

# symbol for portal entrance/exit
T = "  "

########## global variables

movesRemaining = MOVES_ALLOWED    # num moves remaining to complete mission

playerRow = PLAYER_START_ROW      # player row #
playerCol = PLAYER_START_COL      # player column #
patient1Row = random.randint(1, ROWS - 2)       # patient1 row #
patient1Col = random.randint(1, COLUMNS - 2)    # patient1 column #
bomb1Row = random.randint(1, ROWS - 2)        # bomb1 row #
bomb1Col = random.randint(1, COLUMNS - 2)     # bomb1 column #
hiddenBomb1Row = random.randint(1, ROWS - 2)        # hidden bomb1 row #
hiddenBomb1Col = random.randint(1, COLUMNS - 2)     # hidden bomb1 column #
gameStatus = ""                   # game status (win, lose)
isGameOver = False                # flag variable to control game loop  
message = ""                      # error message to display to user

########## functions

def displayStatusPanel():
  # display status panel
  print("\033[" + str(VERTICAL_OFFSET_STATUS_PANEL) + ";0H")
  print()
  if message != "":
    print("Message: " + message)

def displayText(text, lineNum, colorCode):
  # display text on line number, lineNum, with the ANSI color colorCode

  # set color
  print("\033[" + str(colorCode) + "m", end = "")   

  # position cursor to beginning of specified line
  print("\033[" + str(lineNum) + ";0H", end = "")

  print(text)

  # reset color (0)
  print("\033[0m")

########### main program

###### initial setup

# hide cursor (use h instead of l to show cursor)
print("\033[?25l")    

displayText(TITLE, 1, 36)

displayText(INSTRUCTIONS, 2, 37)

# position cursor to location of board
print("\033[" + str(VERTICAL_OFFSET_BOARD) + ";0H", end = "")

# create the gameboard as a list of lists (2D list)
gameboard = [[F] * COLUMNS for i in range(ROWS)]

# draw borders
for k in range(COLUMNS):
  gameboard[0][k]=B
  gameboard[ROWS - 1][k] = B
for m in range(ROWS):
  gameboard[m][0] = B
  gameboard[m][COLUMNS - 1] = B

# place the player's symbol
gameboard[playerRow][playerCol] = P

# place the patient's symbol
gameboard[patient1Row][patient1Col] = E

# place exposed bomb 
gameboard[bomb1Row][bomb1Col] = M

# place hidden bomb 
gameboard[hiddenBomb1Row][hiddenBomb1Col] = H

# place portals on border 
gameboard[PORTAL1A_ROW][COLUMNS - 1] = T
gameboard[PORTAL1B_ROW][0] = T

# display the initial board
for row in range(ROWS):
  for col in range(COLUMNS):
    print(gameboard[row][col], end = "")
  print()

displayStatusPanel()


############ main game loop

while not isGameOver:
  previousPlayerRow = playerRow
  previousPlayerCol = playerCol 
  previousSymbol = gameboard[playerRow][playerCol] 
  playerMove = getkey()
  movesRemaining -= 1

  # player moves right
  if playerMove in [keys.RIGHT, "d"]:

    if playerCol < COLUMNS:
      playerCol += 1
      # don't let player leave board
      if playerCol >= COLUMNS - 1:
        playerCol = COLUMNS - 1

  # player moves left
  elif playerMove in [keys.LEFT, "a"]:
    
    if playerCol > 0:
      playerCol -= 1
      # don't let player leave board
      if playerCol <= 0:
        playerCol = 0

  # player moves down
  elif playerMove in [keys.DOWN, "s"]:
   
    if playerRow < ROWS - 1:
      playerRow += 1
      # don't let player leave board
      if playerRow >= ROWS:
        playerRow = ROWS - 1

  # player moves up
  elif playerMove in [keys.UP, "w"]:
    if playerRow > 0:
      playerRow -= 1  
      # don't let player leave board
      if playerRow <= 0:  
        playerRow = 0

  # win detection
  if gameboard[playerRow][playerCol] == E:
    message = "You saved the patient."
    gameStatus = "win"
    isGameOver = True

  # collision detection with borders or explosed bombs
  elif gameboard[playerRow][playerCol] in [B, M, H]:
    message = "Game over."
    gameStatus = "lose"
    isGameOver = True

  # moving through portal 1
  elif gameboard[playerRow][playerCol] in [T]:
    if playerRow == PORTAL1A_ROW and playerCol == PORTAL1A_COL:
      playerRow = PORTAL1B_ROW
      playerCol = PORTAL1B_COL
    elif  playerRow == PORTAL1B_ROW and playerCol == PORTAL1B_COL:
      playerRow = PORTAL1A_ROW
      playerCol = PORTAL1A_COL

  # check remaining moves
  if movesRemaining <= 0:
    message = "You ran out of moves. Game Over."
    gameStatus = "lose"
    isGameOver = True

  gameboard[playerRow][playerCol] = P
  gameboard[previousPlayerRow][previousPlayerCol] = F

  buffer = ""

  # previous row from player's current position
  for col in range(COLUMNS):
    if playerRow > 0:
      buffer += (gameboard[playerRow - 1][col] )
  buffer += "\n"

  # row of player's current position
  for col in range(COLUMNS):
    buffer += (gameboard[playerRow][col] )
  buffer += "\n"

  # next row after player's current position
  for col in range(COLUMNS):
    if playerRow < ROWS - 1:
      buffer += (gameboard[playerRow + 1][col] )

  # print area of board above 1-3 rows 
  # around player's current position
  print("\033[" + str(playerRow - 1 + VERTICAL_OFFSET_BOARD) + ";0H", end = "")
  
  # print the rows where the player moved
  print(buffer)
  
  displayStatusPanel()
  
