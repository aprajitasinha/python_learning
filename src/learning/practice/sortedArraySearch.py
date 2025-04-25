class sortedArray:
    def __init__(self) -> None:
        pass
    
    def getSortedArray(self,arr,k):
        for i in range(len(arr)):
            if arr[i]==k:
                return True
        return False
    
if __name__=="__main__":
    g=sortedArray()
    print(g.getSortedArray([1, 2, 3, 4, 5], 6)) 
        