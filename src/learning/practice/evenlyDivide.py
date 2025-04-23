class evenlyDivide:
    def __init__(self) -> None:
        pass
    
    def getEvenlyDivide(self,n):
        count=0
        for digit in str(n):
            d=int(digit)
            if d!=0 and n%d==0:
                count+=1
        return count

if __name__=="__main__":
    g=evenlyDivide()
    print(g.getEvenlyDivide(10))
    