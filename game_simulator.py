#Game Simulator for PoolballGMs
from logging import StringTemplateStyle
from player_class import *

team1 = []
for i in range(6):
    p1 = Player(randint(4,5),randint(0,1),randint(1,4))
    for j in range(randint(5,7)):
        p1.age_player()
    team1.append(p1)

team2 = []
for i in range(6):
    p2 = Player(randint(1,5),randint(0,1),randint(1,4))
    for j in range(randint(2,7)):
        p2.age_player()
    team2.append(p2)

#Line 1
c1 = team1[0]
s1 = team1[1]
d1 = team1[2]
rng1 = randint(10,20)
score1 = 0

print(rng1)
print(str(c1) + " {0} {1} {2}".format(c1.gsss,c1.pmss,c1.dbss))
print(str(s1) + " {0} {1} {2}".format(s1.gsss,s1.pmss,s1.dbss))
print(str(d1) + " {0} {1} {2}".format(d1.gsss,d1.pmss,d1.dbss))
print()

c2 = team2[0]
s2 = team2[1]
d2 = team2[2]
rng2 = randint(10,20)
score2 = 0

print(rng2)
print(str(c2) + " {0} {1} {2}".format(c2.gsss,c2.pmss,c2.dbss))
print(str(s2) + " {0} {1} {2}".format(s2.gsss,s2.pmss,s2.dbss))
print(str(d2) + " {0} {1} {2}".format(d2.gsss,d2.pmss,d2.dbss))
print()

#Team 1
plays = 0
plays += math.floor((c1.pmss-50)*rng1*0.02)
plays += math.floor((s1.pmss-50)*rng1*0.02)
plays += math.floor((d1.pmss-50)*rng1*0.02)

cplays = math.floor(0.5*plays)
splays = math.floor(0.3*plays)
dplays = math.floor(0.2*plays)

cshots = math.floor(cplays*(c1.gsss**1.5)*0.001)
sshots = math.floor(splays*(s1.gsss**1.5)*0.001)
dshots = math.floor(dplays*(d1.gsss**1.5)*0.001)

goalPercent = 1-(((0.5*d2.dbss)+(0.3*s2.dbss)+(0.2*c2.dbss))*0.01)

cgoals = math.floor(cshots*goalPercent)
sgoals = math.floor(sshots*goalPercent)
dgoals = math.floor(dshots*goalPercent)

print("{0}, {1}, {2}".format(cgoals,sgoals,dgoals))
score1 += cgoals+sgoals+dgoals

#Team 2
plays = 0
plays += math.floor((c2.pmss-50)*rng1*0.02)
plays += math.floor((s2.pmss-50)*rng1*0.02)
plays += math.floor((d2.pmss-50)*rng1*0.02)

cplays = math.floor(0.5*plays)
splays = math.floor(0.3*plays)
dplays = math.floor(0.2*plays)

cshots = math.floor(cplays*(c2.gsss**1.5)*0.001)
sshots = math.floor(splays*(s2.gsss**1.5)*0.001)
dshots = math.floor(dplays*(d2.gsss**1.5)*0.001)

goalPercent = 1-(((0.5*d1.dbss)+(0.3*s1.dbss)+(0.2*c1.dbss))*0.01)

cgoals = math.floor(cshots*goalPercent)
sgoals = math.floor(sshots*goalPercent)
dgoals = math.floor(dshots*goalPercent)

print("{0}, {1}, {2}".format(cgoals,sgoals,dgoals))
score2 += cgoals+sgoals+dgoals

print()

#Line 2
c1 = team1[3]
s1 = team1[4]
d1 = team1[5]
rng1 = randint(10,20)

print(rng1)
print(str(c1) + " {0} {1} {2}".format(c1.gsss,c1.pmss,c1.dbss))
print(str(s1) + " {0} {1} {2}".format(s1.gsss,s1.pmss,s1.dbss))
print(str(d1) + " {0} {1} {2}".format(d1.gsss,d1.pmss,d1.dbss))
print()

c2 = team2[3]
s2 = team2[4]
d2 = team2[5]
rng2 = randint(10,20)

print(rng2)
print(str(c2) + " {0} {1} {2}".format(c2.gsss,c2.pmss,c2.dbss))
print(str(s2) + " {0} {1} {2}".format(s2.gsss,s2.pmss,s2.dbss))
print(str(d2) + " {0} {1} {2}".format(d2.gsss,d2.pmss,d2.dbss))
print()

#Team 1
plays = 0
plays += math.floor((c1.pmss-50)*rng1*0.02)
plays += math.floor((s1.pmss-50)*rng1*0.02)
plays += math.floor((d1.pmss-50)*rng1*0.02)

cplays = math.floor(0.5*plays)
splays = math.floor(0.3*plays)
dplays = math.floor(0.2*plays)

cshots = math.floor(cplays*(c1.gsss**1.5)*0.001)
sshots = math.floor(splays*(s1.gsss**1.5)*0.001)
dshots = math.floor(dplays*(d1.gsss**1.5)*0.001)

goalPercent = 1-(((0.5*d2.dbss)+(0.3*s2.dbss)+(0.2*c2.dbss))*0.01)

cgoals = math.floor(cshots*goalPercent)
sgoals = math.floor(sshots*goalPercent)
dgoals = math.floor(dshots*goalPercent)

print("{0}, {1}, {2}".format(cgoals,sgoals,dgoals))
score1 += cgoals+sgoals+dgoals

#Team 2
plays = 0
plays += math.floor((c2.pmss-50)*rng1*0.02)
plays += math.floor((s2.pmss-50)*rng1*0.02)
plays += math.floor((d2.pmss-50)*rng1*0.02)

cplays = math.floor(0.5*plays)
splays = math.floor(0.3*plays)
dplays = math.floor(0.2*plays)

cshots = math.floor(cplays*(c2.gsss**1.5)*0.001)
sshots = math.floor(splays*(s2.gsss**1.5)*0.001)
dshots = math.floor(dplays*(d2.gsss**1.5)*0.001)

goalPercent = 1-(((0.5*d1.dbss)+(0.3*s1.dbss)+(0.2*c1.dbss))*0.01)

cgoals = math.floor(cshots*goalPercent)
sgoals = math.floor(sshots*goalPercent)
dgoals = math.floor(dshots*goalPercent)

print("{0}, {1}, {2}".format(cgoals,sgoals,dgoals))
score2 += cgoals+sgoals+dgoals


print("Final score: {0} to {1}".format(score1,score2))