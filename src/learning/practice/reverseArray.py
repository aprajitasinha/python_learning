class reverseArray:
    def __init__(self) -> None:
        pass
    
    def reverseAnArray(self,arr):
        return arr[::-1]

if __name__=="__main__":
    g=reverseArray()
    print(g.reverseAnArray([1,4,5,6,3]))