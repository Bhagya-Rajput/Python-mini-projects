def board():
   lst =[x for x in range(9)]
   for i in range(3):
      for j,k in zip(range(3),lst[i*3:(i+1)*3]):
         print(f" {k} ", end = "|"if j<2  else '\n')
      print("----------" if i<2 else "")
board()
