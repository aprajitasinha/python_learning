class largestElement:
    def __init__(self) -> None:
        pass
    
    def getLargestelement(self,arr):
        arr.sort()
        for _ in arr:
            return arr[-1]

if __name__=="__main__":
    g=largestElement()
    print(g.getLargestelement([16, 17, 4, 3, 5, 2]))