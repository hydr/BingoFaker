# -*- coding: utf-8 -*-
__author__ = 'Maximilian Balbach'


import numpy as np
maxNumber = 80

class bingo:


    def __init__(self):
        #Generate Bingo card
        a = np.arange(1,maxNumber)
        np.random.shuffle(a)
        b = a[:25]
        self.field = b.reshape((5,5))
        self.hits = np.zeros((5,5),bool)

    def GenerateFakedCard(self, numbers, bingoIndex):
        #make empty field
        self.field = np.zeros((5,5), int)

        #chose bingo numbers
        shuffle = numbers[:bingoIndex-1]
        np.random.shuffle(shuffle)
        bingoNumbers = np.append(shuffle[:4], numbers[bingoIndex])

        #Get fill numbers
        fillNumbers = np.concatenate((shuffle[5:], numbers[bingoIndex+1:]))
        np.random.shuffle(fillNumbers)

        #Choose Bingo row and write Bingo to it
        rand = np.random.randint(12)
        print rand
        if rand in range(5):
            self.field[rand,:] = bingoNumbers
        elif rand in range(5,10):
            self.field[:,rand-5] = bingoNumbers
        elif rand == 10:
            self.field[(0,1,2,3,4),(0,1,2,3,4)] = bingoNumbers
        elif rand == 11:
            self.field[(0,1,2,3,4),(4,3,2,1,0)] = bingoNumbers
        print self.field

        #Fill with other numbers
        for i in range(self.field.size):
            if self.field.flat[i] == 0:
                self.field.flat[i] = fillNumbers[i]

        #check for ealier Bingo
        self.CalculateHits(numbers[:bingoIndex-1])
        print self.hits

        if self.CheckBingo():
            print "Zu verwerfen"
        else:
            print "OK"



    def CheckUniqueness(self):
        a = self.field.flatten()
        a.sort(axis=0)
        if a.size != np.unique(a).size:
            return False

        return True

    def UpdateHits(self, number):
         for i in range(self.field.size):
             if self.field.flat[i] == number:
                 self.hits.flat[i] = True

    def CalculateHits(self, numbers):
        for i in range(self.field.size):
             if self.field.flat[i] in numbers:
                 self.hits.flat[i] = True


    def CheckBingo(self):
        #check horizontal bingos
        if np.any(np.all(self.hits, axis=0)):
            return True
        #check vertical bingos
        if np.any(np.all(self.hits, axis=1)):
            return True
        #check diagonal bingos
        if np.all(np.diagonal(self.hits)) or np.all(np.diagonal(np.fliplr(self.hits))):
            return True

        return False



if __name__ == "__main__":
    print "hallo"

    drawn = np.arange(1,maxNumber)
    np.random.shuffle(drawn)

    bingoIndex = 25
    print drawn[0:bingoIndex]
    a = bingo()
    a.GenerateFakedCard(drawn, bingoIndex)
    print a.field


    """
    rounds = np.empty(0, int)
    for k in range(100):
        a = bingo()
        for i in range(drawn.size):
            a.UpdateHits(drawn[i])
            if a.CheckBingo():
                print i
                rounds = np.append(rounds, i)
                print drawn[:i+1]
                print a.field
                print a.hits
                break


    print rounds
    print np.mean(rounds)
    print np.min(rounds)
    """
    #Test
    """
    a.hits = np.array([[False, True, False, True, True],
              [False, True, False, True, True],
              [False, True, False, True, False],
              [False, True, False, True, False],
              [False, True, False, False, False]])

    print a.CheckBingo()
    """


