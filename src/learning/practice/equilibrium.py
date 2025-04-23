class equilibrium:
    def __init__(self) -> None:
        pass
    
    def findEquilibrium(self, arr):
        n=len(arr)
        total_sum=sum(arr)
        left_sum=0
        for i in range(n):
            right_sum=total_sum-left_sum-arr[i]
            if left_sum==right_sum:
                return i
            left_sum+=arr[i]
        return -1
    
if __name__=="__main__":
    g=equilibrium()
    print(g.findEquilibrium([1, 2, 0, 3]))