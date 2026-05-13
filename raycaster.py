from math import *


class Raycaster():
    def __init__(self, radius=0):
        self.x = 0
        self.y = 0
        self.radius = radius


    def raycast(self, x, y, direction, VisionWidth, allblocks, renderDistance, speed=1, dirspeed=1):
        All = allblocks
        Direction = direction - VisionWidth / 2
        data = []

        
        newAll = []
        for i in range(len(All)):
            calc = sqrt(pow(abs(All[i][0][0][0] - All[i][0][1][0]), 2) + pow(abs(All[i][0][0][1] - All[i][0][1][1]), 2)) / 2
            calc2 = [(All[i][0][0][0] + All[i][0][1][0])/2, (All[i][0][0][1] + All[i][0][1][1])/2]
            # print(calc)
            # print(sqrt(pow(abs(calc2[0] - x), 2) + pow(abs(calc2[1] - y), 2)) - calc - self.radius, renderDistance * speed)
            if sqrt(pow(abs(calc2[0] - x), 2) + pow(abs(calc2[1] - y), 2)) - calc - self.radius <= renderDistance * speed:
                newAll.append(All[i])
        
        All = newAll
        distance = 0
        boolean = False
        for i in range(floor(VisionWidth * floor(1/dirspeed))):
            

            self.x = x
            self.y = y
            distance = 0

            for j in range(renderDistance):
    
                boolean = False
                
                for k in range(len(All)):
                    boolean = self.collision(All[k][0][0][0], All[k][0][0][1], All[k][0][1][0], All[k][0][1][1])
                    if boolean:
                        break
                if boolean:
                    break
                else:
                    self.x += cos(radians(Direction)) * speed
                    self.y += sin(radians(Direction)) * speed
                    distance += speed
            if boolean == False:
                    distance = None
            if len(All) != 0:
                data.append([distance, All[k][1]])
            Direction += dirspeed

        return data


    def collision(self, x, y, x2, y2):
        if self.x + self.radius <= x2 and self.x - self.radius >= x:
            if self.y + self.radius <= y2 and self.y - self.radius >= y:
                return True
        return False
