class arraySubset:
    def __init__(self) -> None:
        pass
    
    def getAraySubset(sef,arr1,arr2):
        freq={}
        for num in arr1:
            freq[num]=freq.get(num,0)+1
        for num in arr2:
            if freq.get(num,0)==0:
                return False
            freq[num]-=1
        return True
    
if __name__=="__main__":
    g=arraySubset()
    print(g.getAraySubset([1, 5, 10, 20, 40, 80] ,[6, 7, 20, 80, 100] ))