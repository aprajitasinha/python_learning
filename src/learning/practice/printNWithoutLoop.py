class PrintNWithoutLoop:
    def __init__(self) -> None:
        pass
    
    def withoutLoop(self,n):
    ##print n without loop
        if n==0:
            return
        self.withoutLoop(n-1)
        print(n,end=" ")  

if __name__=="__main__":
    g=PrintNWithoutLoop()
    n=("Enter the number: ",g.withoutLoop(8))
    
        
        