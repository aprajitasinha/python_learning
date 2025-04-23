class secondLargest:
    def __init__(self) -> None:
        pass

    def getSecondLargest( self,arr):
            # Code Here
        if len(arr)<2:
            return -1
        first =float('-inf')
        second= float('-inf')
        for num in arr: 
            if num >first:
                second=first
                first=num
            if num >second and num<first:
                second=num
        return second if second!=float('-inf') else -1
    
if __name__=="__main__":
    g=secondLargest()
    print(g.getSecondLargest([1, 2, 3, 5]))
    