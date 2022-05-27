#Main Method for PoolballGMs
from player_class import *

for j in range(5):
  for k in range(4):
    for l in range(2):
      g = []
      p = []
      d = []

      for i in range(50000):
        p1 = Player(j+1,l,k+1)

        if (l == 0):
          for m in range(7):
            p1.age_player()

        else:
          for m in range(8):
            p1.age_player()
        
        g.append(p1.gsss)
        p.append(p1.pmss)
        d.append(p1.dbss)

      avgG = sum(g)/len(g)
      avgP = sum(p)/len(p)
      avgD = sum(d)/len(d)

      print(p1, end="")
      print(" {0} stars, top={1} ||| {2} {3} {4}".format(p1.stars, p1.top, avgG, avgP, avgD))