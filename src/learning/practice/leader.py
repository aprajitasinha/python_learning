class leader:
    def __init__(self) -> None:
        pass
    
    def get_leaders( self,arr):
        # code here
        n=len(arr)
        max_from_right=arr[-1]
        leader=[]
        leader.append(max_from_right)
        for i in range(n-2,-1,-1):
            if arr[i]>=max_from_right:
                max_from_right=arr[i]
                leader.append(max_from_right)
        return leader[::-1]

if __name__=="__main__":
    g=leader()
    print(g.get_leaders([1, 2, 3, 5]))