import math
class squareRoot:
    def __init__(self, number):
        self.number = number

    def floorSqrt(self):
        return math.floor(math.sqrt(self.number))


if __name__=="__main__":
    g=squareRoot(10)
    print(g.floorSqrt())
    
        
        