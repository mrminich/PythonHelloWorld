# REPLACE THIS WITH YOUR NAME

# WORKS CITED:
# using color 
# https://ozzmaker.com/add-colour-to-text-in-python/
# using emojis
# https://www.geeksforgeeks.org/python-program-to-print-emojis/ 
# https://unicode.org/emoji/charts/full-emoji-list.html
# REPLACE THIS WITH WEBSITE LINKS OR NAMES OF CLASSMATE HELPERS

# UPGRADES: 
# REPLACE THIS WITH A DESCRIPTION OF YOUR UPGRADE(S)

######### imports

from os import system           # for system("clear")
from getkey import getkey, keys # for getkey & use arrow keys

######### constants 

TITLE = "Simple Maze"
INSTRUCTIONS = "Use the arrow keys to reach the \N{cheese wedge} !"

# num of lines from top of screen for the title
VERTICAL_OFFSET_TITLE = 1 

# num of lines from top of screen for the maze board    
VERTICAL_OFFSET_MAZE = 5   

# num of lines from top of screen for the status panel
VERTICAL_OFFSET_STATUS_PANEL = 15   

# num of moves player has to complete the maze w/o losing
MOVES_ALLOWED = 20

# maze height (# of rows), must match gameboard
ROWS = 10 

# maze width (# of columns), must match gameboard            
COLUMNS = 10           

PLAYER_START_ROW = 1  # row # of player's starting position
PLAYER_START_COL = 1  # column # of player's starting position

# 2 characters must be used for the following symbols
# if necessary, add a space such as "* " rather than just "*"

# fill character for empty positions
F = "  "               

# player's symbol
P = "\N{mouse face} "                         

# vertical wall symbol
V = "\033[0;36;46m" + "| " + "\033[0m"        

# horizontal wall symbol
H = "\033[0;36;46m" + "- " + "\033[0m"        

# symbol for border
B = "\033[0;36;46m" + "* " + "\033[0m"                              

# symbol for the end of the maze
E = "\N{cheese wedge} "     

# symbol for portal entrance/exit
T = ">>"

########## global variables

movesRemaining = MOVES_ALLOWED    # num moves remaining to complete maze

playerRow = PLAYER_START_ROW      # player row #
playerCol = PLAYER_START_COL      # player column #
gameStatus = ""                   # game status (win, lose)
isGameOver = False                # flag variable to control game loop  
message = ""                      # error message to display to user

# make sure that the correct symbols are placed in desired rows and columns
gameboard = [
  # columns
  # 0 1 2 3 4 5 6 7 8 9  # rows
   [B,B,B,B,B,B,B,B,B,B],  # 0 
   [B,P,V,F,F,F,F,F,F,B],  # 1 
   [B,F,V,F,H,H,H,H,F,B],  # 2
   [B,F,V,F,V,T,F,V,T,B],  # 3
   [B,F,V,F,V,H,F,V,H,B],  # 4
   [B,F,V,F,F,F,F,F,F,B],  # 5
   [B,F,F,F,H,V,F,V,F,B],  # 6
   [B,F,V,H,H,H,F,V,F,B],  # 7
   [B,F,V,F,F,F,F,V,E,B],  # 8
   [B,B,B,B,B,B,B,B,B,B],  # 9
]

########## functions

def displayStatusPanel():
  # display status panel
  print("\033[" + str(VERTICAL_OFFSET_STATUS_PANEL) + ";0H")
  print("Remaining Moves: " + str(movesRemaining) + " out of " + str(MOVES_ALLOWED))
  print("Current Location: Row " + str(playerRow) + " Column " + str(playerCol))
  print()
  if message != "":
    print("Message: " + message)

########### main program

###### initial setup

# hide cursor (use h instead of l to show cursor)
print("\033[?25l")  

# clear screen, 2J resets cursor to top left corner
print("\033[2J", end = "")    

 # set title color (36) & turn on underlining (4)
print("\033[36m\033[4m", end = "")  

# position cursor to location for the title
print("\033[" + str(VERTICAL_OFFSET_TITLE) + ";0H", end = "")

print(TITLE)

# turn off underline (24), reset color (0)
print("\033[24m\033[0m") 

print(INSTRUCTIONS)

# position cursor to location of maze
print("\033[" + str(VERTICAL_OFFSET_MAZE) + ";0H", end = "")

# place the player's symbol in the maze
gameboard[playerRow][playerCol] = P

# display the initial maze
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
      # don't let player leave maze
      if playerCol >= COLUMNS - 1:
        playerCol = COLUMNS - 1

  # player moves left
  elif playerMove in [keys.LEFT, "a"]:
    
    if playerCol > 0:
      playerCol -= 1
      # don't let player leave maze
      if playerCol <= 0:
        playerCol = 0

  # player moves down
  elif playerMove in [keys.DOWN, "s"]:
   
    if playerRow < ROWS - 1:
      playerRow += 1
      # don't let player leave maze
      if playerRow >= ROWS:
        playerRow = ROWS - 1

  # player moves up
  elif playerMove in [keys.UP, "w"]:
    if playerRow > 0:
      playerRow -= 1  
      # don't let player leave maze
      if playerRow <= 0:  
        playerRow = 0

  # win detection
  if gameboard[playerRow][playerCol] == E:
    message = "You won. Congratulations."
    gameStatus = "win"
    isGameOver = True

  # collision detection with walls
  elif gameboard[playerRow][playerCol] in [B, H, V]:
    message = "You hit a wall. Game over."
    gameStatus = "lose"
    isGameOver = True

  # entrance into portal
  # TODO - fix the current limitation that portal's have to be 
  # within one row of each other & they are erased by the player
  elif gameboard[playerRow][playerCol] in [T]:
    message = "You made it through the portal."
    if playerRow == 3 and playerCol == 8:
      gameboard[3][8] = T
      playerRow = 3
      playerCol = 5
    elif  playerRow == 3 and playerCol == 5:
      gameboard[3][5] = T 
      playerRow = 3
      playerCol = 8

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
  print("\033[" + str(playerRow - 1 + VERTICAL_OFFSET_MAZE) + ";0H", end = "")
  
  # print the rows where the player moved
  print(buffer)
  
  displayStatusPanel()
  
