#2 player tic tac toe

#Start of program
playAgain = True
board = [" "] * 10
isWinner = False
correctMoves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
playAgainAskInputs = ["Y", "N"]

#Custom functions

def p1Turn():
  print("Player 1 Turn")
  p1Move = input("Where do you want to play?")
  while p1Move not in correctMoves:
    print("Invalid Move")
    print()
    print("Player 1 Turn")
    print()
    p1Move = input("Where do you want to play?")
  checkMove(p1Move, "X")

def p2Turn():
  print("Player 2 Turn")
  p2Move = input("Where do you want to play?")
  while p2Move not in correctMoves:
    print("Invalid Move")
    print()
    print("Player 2 Turn")
    print()
    p2Move = input("Where do you want to play?")
  checkMove(p2Move, "O")

def drawBoard():
  global board
  print('')
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-----')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-----')
  print(board[1] + '|' + board[2] + '|' + board[3])

def checkMove(move, symbol):
  print("Checking move...")
  if board[int(move)] == " ":
    board[int(move)] = symbol
  else:
    print("That spot is already taken")
    if symbol == "X":
      p1Turn()
    else:
      p2Turn()

def checkWin():
  print("Checking for a winner...")
  if board[7] == board[8] and board[8] == board[9] and board[7] != " ":
    return board[7]
  elif board[4] == board[5] and board[5] == board[6] and board[4] != " ":
    return board[4]
  elif board[1] == board[2] and board[2] == board[3] and board[1] !=" ":
    return board[1]
  elif board[7] == board[4] and board[4] == board[1] and board[7] !=" ":
    return board[7]
  elif board[8] == board[5] and board[5] == board[2] and board[8] !=" ":
    return board[8]
  elif board[9] == board[6] and board[6] == board[3] and board[9] !=" ":
    return board[9]
  elif board[7] == board[5] and board[5] == board[3] and board[7] !=" ":
    return board[7]
  elif board[9] == board[5] and board[5] == board[1] and board[9] !=" ":
    return board[9]

#Play again loop
while playAgain == True:


  while isWinner == False:
    p1Turn()
    drawBoard()
    #Check player 1 win
    if checkWin() == "X":
      print("Player 1 Wins!")
      isWinner = True
      while isWinner == True:
        playAgainAsk = input("Do you want to play again? (Y) (N)")
        while playAgainAsk not in playAgainAskInputs:
          print("Invalid Input")
          print()
          playAgainAsk = input("Do you want to play again? (Y) (N)")
        if playAgainAsk == "Y":
          playAgain = True
          isWinner = False
          board = [" "] * 10
        elif playAgainAsk == "N":
          playAgain = False
          isWinner = " "
    p2Turn()
    drawBoard()
    #Check player 2 win
    if checkWin() == "O":
      print("Player 2 Wins!")
      isWinner = True
      while isWinner == True:
        playAgainAsk = input("Do you want to play again? (Y) (N)")
        while playAgainAsk not in playAgainAskInputs:
          print("Invalid Input")
          print()
          playAgainAsk = input("Do you want to play again? (Y) (N)")
        if playAgainAsk == "Y":
          playAgain = True
          isWinner = False
          board = [" "] * 10
        elif playAgainAsk == "N":
          playAgain = False
          isWinner = " "
  if playAgain == False:
    print("Thanks for playing!")
