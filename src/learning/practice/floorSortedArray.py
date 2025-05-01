class FloorSortedArray:
    
    def __init__(self) -> None:
        pass
    
    def getFloorSortedArray(self,arr,x):
        n=len(arr)
        ##we can get multiple floor values from the array we need the last one
        floor=[]
        for i in range(n):
            if arr[i]<=x:
                floor.append(i)
        if len(floor)==0:
            return -1
        else:
            return max(floor)
if __name__=="__main__":
    g=FloorSortedArray()
    print(g.getFloorSortedArray([1, 2, 8, 10, 10, 12, 19],11))
    
                