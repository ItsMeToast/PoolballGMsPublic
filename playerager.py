#Takes in a player, and ages them one year
#Mostly to show Sam the process, or age players manually
from player_class import *

#Get player
print("Enter: First Name")
fname = input()

print("Enter: Last Name")
lname = input()

print("Enter: Age")
age = int(input())

print("Enter: Position (1 GS, 2 PM, 3 DB, 4 AA)")
pos = int(input())

print("Enter: Stars (1 very weak, 2 weak, 3 moderate, 4 strong, 5 very strong)")
stars = int(input())

print("Enter: Top Prospect? (0 no, 1 yes)")
top = int(input())

print("Enter: EX, ST, AC, RX, SZ, IQ (press enter after each stat)")
ex = int(input())
st = int(input())
ac = int(input())
rx = int(input())
sz = int(input())
iq = int(input())

print("Enter: Injury%")
injury = int(input())

#Create player
#need to look at better ways to create an existing player (maybe?)
p1 = Player(1,1,1)
p1.set_stats(fname, lname, pos, stars, top, age, ex, st, ac, rx, sz, iq, injury)

print("\nCurrent Player Stats:")
print("{0} {1} {2} {3} {4}".format(p1, p1.gsss, p1.pmss, p1.dbss, p1.stat_string()))

print("\nNew Player Stats:")
times = 29-p1.age
for i in range(times):
    p1.age_player()
    print("{0} {1} {2} {3} {4}".format(p1, p1.gsss, p1.pmss, p1.dbss, p1.stat_string()))

print()