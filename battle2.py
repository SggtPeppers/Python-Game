from random import randint
import os
print("^"*50)
print("Welcome to the most Badass Battleship ever!!")
print("^"*50)
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  x = " "
  for row in board:
    print (x.join(row))
    
print("\n")
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def music():
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.35, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.35, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.4, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.4, 659.2551))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.6, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.35, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.35, 659.2551))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.6, freq))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.35, 783.9908))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.6, 880))
  os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.5, 783.9908))


ship_row = random_row(board)
ship_col = random_col(board)







for turn in range(4):
  print ("Turn", turn + 1)
  print("\n")
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("-"*42)
    print ("Congratulations! You sank my battleship!")
    print("-"*42)
    board[guess_row][guess_col] = "⛵" 
    print_board(board)
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("\n")
      print("-"*35)
      print ("Oops, that's not even in the ocean.")
      print("-"*35)
      print("\n")
    elif board[guess_row][guess_col] == "X":
      print("\n")
      print("-"*29)
      print( "You guessed that one already." )
      print("-"*29)
      print("\n")
    elif guess_row == ship_row -1 and guess_col == ship_col-1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row +1 and guess_col == ship_col+1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row +1 and guess_col == ship_col-1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row -1 and guess_col == ship_col+1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row +1 and guess_col == ship_col:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row and guess_col == ship_col+1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row -1 and guess_col == ship_col:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    elif guess_row == ship_row and guess_col == ship_col-1:
      print("-"*41)
      print("THAT WAS CLOSEE! But you need to aim again")
      print("-"*41)
      board[guess_row][guess_col] = "⏿"
    else:
      print("\n")
      print("-"*25)
      print ("You missed my battleship!")
      print("-"*25)
      print("\n")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3 :
      print("-"*25)
      print("Game Over")
      print("-"*25)
      duration = 0.6
      freq = 698.4564

      music()
      music()





