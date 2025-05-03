class RotatingArray():
    
    def _init__(self):
        pass
    
    ## Function to left rotate arr[] of size n by d
    def leftRotate(self,arr, d):
        n = len(arr)
        d = d % n
        arr = arr[d:] +arr[:d]
        return arr
    
if __name__ == "__main__":
    arr = [1, 3, 4, 2]
    d = 3
    g = RotatingArray()
    print(g.leftRotate(arr,d))
        
        
        
        