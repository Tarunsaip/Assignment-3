import random
import copy
import math

count = 0
def C2n(n):
    'returns C(2,n)'
    return n * (n-1) / 2

class CheckeredPageState:

    def __init__(self, checkeredPage):
        self.checkeredPage = checkeredPage
        self.dimension = len(self.checkeredPage)
        self.setDic()
        self.setHeuristic()

    def setDic(self):
        dicRows = {}
        dicDiagonal1 = {}
        dicDiagonal2 = {}
        for i in range(self.dimension):
            dicRows[i] = 0
            for j in range(self.dimension):
                dicDiagonal1[i-j] = 0
                dicDiagonal2[i+j] = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.checkeredPage[i][j]:
                    dicRows[i] += 1
                    dicDiagonal1[i-j] += 1
                    dicDiagonal2[j+i] += 1
        self.dicRows = dicRows
        self.dicDiagonal1 = dicDiagonal1
        self.dicDiagonal2 = dicDiagonal2

    def setHeuristic(self):
        h = 0
        for key in self.dicRows:
            if self.dicRows[key] > 1:
                h += C2n(self.dicRows[key])
        for key in self.dicDiagonal1:
            if self.dicDiagonal1[key] > 1:
                h += C2n(self.dicDiagonal1[key])
        for key in self.dicDiagonal2:
            if self.dicDiagonal2[key] > 1:
                h += C2n(self.dicDiagonal2[key])
        self.h = h

    def getFirstChoice(self):
        
        test = [[False for i in range(self.dimension)] for j in range(self.dimension)]
        while 1:
            i = random.randrange(0, self.dimension)
            j = random.randrange(0, self.dimension)
            test[i][j] = True
            newCheck = copy.deepcopy(self.checkeredPage)
            newCheck[i][j] = 1
            for k in range(self.dimension):
                if self.checkeredPage[k][j]:
                    ikeep = k
                    break
            newCheck[ikeep][j] = 0
            newCheck[i][j] = 1
            neighbor = CheckeredPageState(newCheck)
            if neighbor.h < self.h:
                return neighbor
            flag = True
            for x in test:
                for y in x:
                    if y is False:
                        flag = False
                        break
                if flag is False:
                    break
            if flag is True:
                return None

    def getMove(self, neighbor):
        global steps
        test = False
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] != neighbor.checkeredPage[i][j]:
                    if self.checkeredPage[i][j] == 1:
                        istart = i
                    else:
                        iend = i
                    if test is False:
                        test = True
                    else:
                        break

def HillCLimbingFirstChoice(checkeredPageInitial):
    global count
    current = CheckeredPageState(checkeredPageInitial)
    while 1:
        neighbor = current.getFirstChoice()
        if neighbor is None:
            if current.h == 0:
                return True, current
            else:
                count += 1
                return False, current
        current.getMove(neighbor)
        current = neighbor


def getRandomCheckeredPage(dimension):
    checkeredPage = [[0 for i in range(dimension)] for j in range(dimension)]
    randNumbers = random.sample(range(0, dimension), dimension)
    for j in range(dimension):
        checkeredPage[randNumbers[j]][j] = 1
    return checkeredPage

for i in range(1000):
    randomCheck = getRandomCheckeredPage(8)
    HillCLimbingFirstChoice(randomCheck)