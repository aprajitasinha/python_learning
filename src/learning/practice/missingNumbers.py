class missingNumber:
    def __init__(self) -> None:
        pass
    
    def missingNumbers( self,arr):
        # code here
        n=len(arr)+1
        total_sum=n*(n+1)//2
        arr_sum=sum(arr)
        return (total_sum-arr_sum)
    

if __name__=="__main__":
    g=missingNumber()
    print(g.missingNumbers([1, 2, 3, 5]))