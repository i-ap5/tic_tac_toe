def main():
  choice = int(input ('Select type\n1. Single Player\n2. Multiplayer\n\t Enter your choice : '))
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice ==1):
    print('AI : 0\tVs\tYou : X')
    player=int(input('Enter 1 to play 1st or 2 to play 2nd : '))
    for i in range(0,9):
      if(analyseboard(board)!=0):
        break
      if((i+player)%==0):
        CompTurn(board)
      else:
        ConstBoard(board)
        User1Turn(board)
  else:
    for i in range(0,9):
      if(analyseboard(board)!=0):
        break
      if((i%2)%==0):
        ConstBoard(board)
        User1(board)
      else:
        ConstBoard(board)
        User2Turn(board)

  x = analyseboard(board)
  if(x==0):
    ConstBoard(board)
    print("Draw!")
  if(x==-1):
    ConstBoard(board)
    print("Player X Wins!")
  if(x==0):
    ConstBoard(board)
    print("Player 0 Wins!")

def ConstBoard(board):
  print("Current state of the board : \n\n")
  for i in range(0,9):
    if((i>0) and (i%3==0)):
      print('\n')
    if(board[i]==0):
      print('-', end ="\t")
    if(board[i]==-1):
      print('X', end ="\t")
    if(board[i]==1):
      print('O', end ="\t")

  print('\n\n')

main()