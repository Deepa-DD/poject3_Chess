

import numpy as np

a=np.array(["♜","♞","♝","♛","♚","♝","♞","♜","♟","♟","♟","♟","♟","♟","♟","♟","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","♙","♙","♙","♙","♙","♙","♙","♙","♖","♘","♗","♔","♕","♗","♘","♖"])
a1=np.reshape(a,(8,8))
print(a1)



a= np.char.replace(a, "_", '+++++++++++++')
          
