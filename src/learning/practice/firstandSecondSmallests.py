class FirstAndSecondMin:
    def __init__(self) -> None:
        pass
    
    def minAnd2ndMin(self,arr):
        arr.sort()
        n=len(arr)
        for i in range(n):
            if arr[i]!=arr[0]:
                return (arr[0],arr[i])
        return -1

if __name__=="__main__":
    g=FirstAndSecondMin()
    arr=[2, 4, 3, 5, 6]
    print(g.minAnd2ndMin(arr))