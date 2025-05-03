class countSmallerElement:
    def __init__(self) -> None:
        pass
    
    def countOfElement(self, x, arr):
        count=0
        for i in arr:
            if i<=x:
                count+=1
        return count

if __name__=="__main__":
    g=countSmallerElement()
    arr= [10, 1, 2, 8, 4, 5]
    x=9
    print(g.countOfElement(x,arr))