class peakElement:
    def __init__(self) -> None:
        pass
    
    def getPeakElement(self,arr):  
        n=len(arr) 
        for i in range(n):
            left=arr[i-1] if i>0 else float('-inf')  
            right=arr[i+1] if i<n -1 else float('-inf')
            if arr[i]>=left and arr[i]>=right:
                return i
        return -1 
    
if __name__=="__main__":
    g=peakElement()
    print(g.getPeakElement([1, 2, 3, 5]))    