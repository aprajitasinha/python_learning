class arraySearch:
    def __init__(self) -> None:
        pass
    
    def arraySerach(self,arr,x):
        n=len(arr)
        for i in range(n):
            if arr[i]==x:
                return i
        return -1

if __name__=="__main__":
    g=arraySearch()
    print(g.arraySerach( [1, 2, 3, 5],5))
    