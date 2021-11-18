def randomSuccessor(self):
        j = random.randrange(0, self.dimension)
        while 1:
            i = random.randrange(0, self.dimension)
            if self.checkeredPage[i][j] != 1:
                break
        for k in range(self.dimension):
            if self.checkeredPage[k][j]:
                break
        newCheckeredPage = copy.deepcopy(self.checkeredPage)
        newCheckeredPage[i][j] = 1
        newCheckeredPage[k][j] = 0
        return CheckeredPageState(newCheckeredPage)


def HillCLimbingSteepestAscent(checkeredPageInitial):
    current = CheckeredPageState(checkeredPageInitial)
    print("start of hill climbing algorithm steepest ascent")
    while 1:
        neighbor = current.getRandomSteepestAscent()
        if neighbor.h >= current.h:
            if current.h == 0:
                return True, current
            else:
                return False, current
        current.getMove(neighbor)
        current = neighbor
        
    def getRandomSteepestAscent(self):
        neighbors = []
        huristic = float("inf")
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 1:
                    ikeep = i
                    break
            for i in range(self.dimension):
                if self.checkeredPage[i][j] == 0:
                    newCheck = copy.deepcopy(self.checkeredPage)
                    newCheck[i][j] = 1
                    newCheck[ikeep][j] = 0
                    neighbor = CheckeredPageState(newCheck)
                    if neighbor.h < huristic:
                        neighbors[:] = []
                        huristic = neighbor.h
                    if neighbor.h == huristic:
                        neighbors.append(neighbor)
        return(random.choice(neighbors))        
