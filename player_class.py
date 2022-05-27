import math
from random import randint
from external_info import *

class Player:
    def __init__(this, stars, top, position):
        this.firstname = fn[randint(0, (len(fn)-1))]
        this.lastname = ln[randint(0, (len(ln)-1))]
        this.age = 20
        this.stats = []
        this.injury = randint(6,9)
        this.stars = round(stars, 1)
        this.top = bool(top)
        this.position = round(position, 1)

        this.stats.append(randint(50, 70)) #Explosiveness
        this.stats.append(randint(50, 70)) #Strength
        this.stats.append(randint(50, 70)) #Accuracy
        this.stats.append(randint(50, 70)) #Reflexes
        this.stats.append(randint(50, 99)) #Size
        this.stats.append(randint(50, 70)) #IQ

        if this.position <= 1: #Goal Scorer
            this.position = 1
            this.stats[4] += 4
            if this.top == True:
                this.stats[1] += 5 

        elif this.position == 2: #Play Maker
            this.stats[4] += 8
            if this.top == True:
                this.stats[5] += 5 
            
        elif this.position == 3: #Defender
            this.stats[4] += 15
            if this.top == True and this.stars == 5:
                this.stats[4] += 10 

        else: #All Around
            this.position = 4
            this.stats[4] += 10

        for i in range(6):
            if this.stats[i] > 99:
                this.stats[i] = 99

        #Set big 3 stats
        this.gsss = math.floor((this.stats[0]+this.stats[1]+this.stats[2])/3)
        this.pmss = math.floor((this.stats[2]+this.stats[3]+this.stats[5])/3)
        this.dbss = math.floor((this.stats[0]+this.stats[3]+this.stats[4])/3)


    #Sets a players stats to specific values
    def set_stats(self, fname, lname, pos, stars, top, age, ex, st, ac, rx, sz, iq, injury):
        self.firstname = fname
        self.lastname = lname
        self.position = int(pos)
        self.stars = int(stars)
        self.top = bool(top)
        self.age = int(age)
        self.stats[0] = int(ex)
        self.stats[1] = int(st)
        self.stats[2] = int(ac)
        self.stats[3] = int(rx)
        self.stats[4] = int(sz)
        self.stats[5] = int(iq)
        self.injury = int(injury)

        self.gsss = math.floor((self.stats[0]+self.stats[1]+self.stats[2])/3)
        self.pmss = math.floor((self.stats[2]+self.stats[3]+self.stats[5])/3)
        self.dbss = math.floor((self.stats[0]+self.stats[3]+self.stats[4])/3)


    #String output for a player
    def __str__(self):
        posName = ""

        if self.position == 1:
            posName = "GS"
        elif self.position == 2:
            posName = "PM"
        elif self.position == 3:
            posName = "DB"
        else:
            posName = "AA"

        return "{0} {1} ({2}, {3})".format(self.firstname,self.lastname,posName,self.age)


    #Outputs the stats of the player
    def stat_string(self):
        return "[{0}, {1}, {2}, {3}, {4}, {5}, {6}]".format(self.stats[0],self.stats[1],self.stats[2],self.stats[3],self.stats[4],self.stats[5], str(self.injury)+"%")


    #Grows a player 1 year
    def age_player(this):
        growth = []
        index = 0
        #this is used to weight the random integer
        injury_change = [0, 1, 1, 1, 1, 2, 2]

        #20 -> 21 -> 22 -> 23 -> 24 -> 25
        if this.age <= 24:
            #Goal Scorer
            if this.position == 1:
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))
                growth.append(0)
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))

            #Play Maker
            elif this.position == 2:
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(0)
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))

            #Defender
            elif this.position == 3:
                growth.append(round((randint(1, 5)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 2)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 2)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 5)*(0.5*this.stars)), None))
                growth.append(0)
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))

            #All Around
            else:
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(round((randint(1, 4)*(0.5*this.stars)), None))
                growth.append(0)
                growth.append(round((randint(1, 3)*(0.5*this.stars)), None))
        
            #Top prospect bonus
            if this.top:
                for i in growth:
                    if index != 4:
                        growth[index] += 1
                        round(growth[index], None)
                    index += 1
                index = 0

            #Change Injury %
            this.injury -= injury_change[randint(0, 6)]
            if this.injury <= 1:
                this.injury = 1

            #Apply growth to stats
            for i in growth:
                this.stats[index]+=i
                if this.stats[index]>=99:
                    this.stats[index]=99
                index += 1
        
        #25 -> 26 -> 27 (-> 28 if TP)
        elif this.age <= 26 or (this.age == 27 and this.top == True):
            growth.append(round((randint(0, 1)+(0.3*this.stars)), None))
            growth.append(round((randint(0, 1)+(0.3*this.stars)), None))
            growth.append(round((randint(0, 1)+(0.3*this.stars)), None))
            growth.append(round((randint(0, 1)+(0.3*this.stars)), None))
            growth.append(0)
            growth.append(round((randint(0, 1)+(0.3*this.stars)), None))
        
            #Change Injury %
            this.injury -= randint(-1, 1)
            if this.injury <= 1:
                this.injury = 1
            elif this.injury >=9:
                this.injury = 9
            
            #Top prospect check and 99 cap
            for i in growth:
                if this.top == True:
                    growth[index] *= 1.3
                    round(growth[index], None)

                this.stats[index]+=i
                if this.stats[index]>=99:
                    this.stats[index]=99
                index += 1


        #Stat regression (27 -> 28 -> 29, only 28 -> 29 for TP)
        else:
            growth.append(round((randint(4, 10)), None)*-1)
            growth.append(round((randint(4, 10)), None)*-1)
            growth.append(round((randint(4, 10)), None)*-1)
            growth.append(round((randint(4, 10)), None)*-1)
            growth.append(0)
            growth.append(round((randint(1, 3)+(0.5*this.stars)), None))

            #Change Injury %
            this.injury += randint(2, 5)
            if this.injury >= 9:
                this.injury = 9
            
            for i in growth:
                if this.top == True and index != 5:
                    growth[index] *= 0.7
                    round(growth[index], None)

                this.stats[index]+=i
                if this.stats[index]>=99:
                    this.stats[index]=99
                index += 1

        this.gsss = math.floor((this.stats[0]+this.stats[1]+this.stats[2])/3)
        this.pmss = math.floor((this.stats[2]+this.stats[3]+this.stats[5])/3)
        this.dbss = math.floor((this.stats[0]+this.stats[3]+this.stats[4])/3)

        this.age += 1