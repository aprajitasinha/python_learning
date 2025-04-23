class powerOfTwo:
    def __init__(self) -> None:
        pass
     
    def powerOfTwo(self,n):
        if n<=0:
            return False
        return (n&(n-1))==0
        
if __name__=="__main__":
    g=powerOfTwo()
    print(g.powerOfTwo(8))