class zerosAtEnd:
    def __init__(self) -> None:
        pass
    
    def zerosAtENd(self,arr):
        n=len(arr)
        j=0
        for i in range(n):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr

if __name__=="__main__":
    g=zerosAtEnd()
    print(g.zerosAtENd([0, 1, 0, 3, 12]))
                
                