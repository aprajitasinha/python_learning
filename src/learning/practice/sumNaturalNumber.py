class sumNatauralNum:
    def __init__(self) -> None:
        pass
    
    def sumNaturalNumber(self,n):
        return n*(n+1)//2

if __name__=="__main__":
    g=sumNatauralNum()
    print(g.sumNaturalNumber(8))