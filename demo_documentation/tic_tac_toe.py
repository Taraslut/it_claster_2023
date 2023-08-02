# Guru99
# Code developed by Guru99.com
# Guru99 tic-tac-toe game
#Get input
def getInput(prompt, cast=None, condition=None, errorMessage=None):
  while True:
      try:
          val = cast(input(prompt))
          assert condition is None or condition(val)
          return val
      except:
          print(errorMessage or "Invalid input.")
# Print the game board
def printBoard(board):
  print()
  for row in board:
      print(*row)
  print()
# Check if player won using the winning combinations
def checkWin(board):
  # Check rows
  for row in range(len(board)):
      for col in range(len(board)-1):
          if board[row][col] == "_" or board[row][col+1] == "_" or board[row][col] != board[row][col+1]:
              break
      else:
          return True
  # Check column numbers
  for col in range(len(board)):
      for row in range(len(board)-1):
          if board[row][col] == "_" or board[row+1][col] == "_" or board[row][col] != board[row+1][col]:
              break
      else:
          return True
  # Check left diagonal
  for cell in range(len(board)-1):
      if board[cell][cell] == "_" or board[cell+1][cell+1] == "_" or board[cell][cell] != board[cell+1][cell+1]:
          break
  else:
      return True
  # Check right diagonal
  for cell in range(len(board)-1):
      emptyCell = board[cell][len(board)-cell-1] == "_" or board[cell+1][len(board)-cell-2] == "_"
      different = board[cell][len(board)-cell-1] != board[cell+1][len(board)-cell-2]
      if emptyCell or different:
          break
  else:
      return True
  # No win
  return False
# Play tic tac toe game
def play():
  # Introduction
  print("------------\nN-DIMENSIONAL TIC TAC TOE game by guru 99.com \n------------")
  # Set up variables
  N = getInput(prompt="Guru99 says>>> Enter N, the dimensions of the board: ",
               cast=int,
               condition=lambda x: x >= 3,
               errorMessage="Invalid input. Please enter an integer greater than or equal to 3 as explained on guru99.com")
  board = [['_'] * N for _ in range(N)]
  used = 0
  turn = 0
  # Play guru99 tic tac toe game in Python using while infinite loop
  while True:
      # Print guru99 tic tac toe game board
      printBoard(board)
      # Get user pick
      pick = getInput(prompt=f"Player {turn+1} - Pick location (row, col): ",
                      cast=lambda line: tuple(map(int, line.split(" "))),
                      condition=lambda pair: min(pair) >= 0 and max(pair) < N and board[pair[0]][pair[1]] == "_",
                      errorMessage="Invalid input. Please enter a valid, unoccupied location as an integer pair.")
      # Populate location
      board[pick[0]][pick[1]] = "X" if turn == 0 else "O"
      used += 1
      # Check for win
      #Guru99 tutorial
      if checkWin(board):
          printBoard(board)
          print(f"Game over, Player {turn+1} wins.")
          break
      # Check for tie
      elif used == N*N:
          printBoard(board)
          print("Game over. Players have tied the match.")
          print("Guru99.com tic tac toe game ")
          break
      # If no win yet, update next user
      turn = (turn+1)%2
  # Check for rematch
  playAgain = getInput(prompt="Play Guru99 tic tac toe_Game again? (y/n): ",
                       cast=str,
                       condition=lambda ans: ans.strip("\n").lower() in {"y", "n"},
                       errorMessage="Invalid input. Please enter 'y' or 'n'.")
  if playAgain == 'n':
      # End the game
      print("\nGuru99 TicTacToe game ended.")
      return
  else:
      # Rematch
      play()
# Main
if __name__ == '__main__':
  play()