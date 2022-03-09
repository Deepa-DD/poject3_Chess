import chess
print("***  WELCOME TO THE CHESS GAME  ***")

board=chess.Board()

print(board)

print("\n\nTHIS IS OUR CHESS BOARD \n\nNOW YOU NEED TO GIVE INSTRUCTIONS LIKE ------\n\nVertically we excess by numbers, from down like - 1,2,3...8\n\nHorizontal we excess by alphabets, from left like - a,b,c...h")

board.legal_moves

m=input("\n\nPlease give your input:   ")
board.push_san(m)
print(board)