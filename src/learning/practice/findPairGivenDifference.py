class FindPairGivenDifference:
    def __init__(self) -> None:
        pass
    
    def findPair(self,arr,k):
        hash_map={}
        for i in range(len(arr)):
            if arr[i] in hash_map:
                return True
            else:
                hash_map[arr[i]+k]=arr[i]
                hash_map[arr[i]-k]=arr[i]
        return False       
        
if __name__=="__main__":
    g=FindPairGivenDifference()
    print(g.findPair( [5, 20, 3, 2, 5, 80],  40))        
        