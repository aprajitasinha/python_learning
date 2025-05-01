class minDiffrence:
    def __init__(self) -> None:
        pass
    
    def find_min_difference(self,arr,m):
        arr.sort()
        n=len(arr)
        min_dif=(float('inf'))
        for i in range(n-m+1):
            diff=arr[i+m-1]-arr[i]
            if diff<min_dif:
                min_dif=diff
        return min_dif
    
if __name__=="__main__":
    g=minDiffrence()
    print(g.find_min_difference([7, 3, 2, 4, 9, 12, 56],2))