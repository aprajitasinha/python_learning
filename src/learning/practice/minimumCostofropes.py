class MinimumCost:
    def __init__(self) -> None:
        pass
    
    def minimumCostOfRopes(self,arr):
        arr.sort()
        cost=0
        while len(arr)>1:
            first=arr[0]
            second=arr[1]
            cost+=first+second
            arr.pop(0)
            arr.pop(0)
            arr.append(first+second)
            arr.sort()
        return cost
    
if __name__=="__main__":
    g=MinimumCost()
    print(g.minimumCostOfRopes([4, 3, 2, 6]))
        