#BEACHTE: Der Einzug für Python hier auf StudIP ist etwas weird 
def ggT(a: int, b: int) -> int:
   while b != 0:
      a, b = b, a % b
   return a

#testcase für debugging
print("Der ggT lautet: ", ggT(48, 18)) #ouput sollte 6 sein :)