class CountOddEven:
    def __init__(self) -> None:
        pass
    
    def countOddEven(self, arr):
        odd = 0
        even = 0
        for i in arr:
            if i %2==0:
                even+=1
            else:
                odd+=1
        return (odd,even)
if __name__=="__main__":
    g=CountOddEven()
    arr=[1,2, 4, 3, 5]
    print(g.countOddEven(arr))