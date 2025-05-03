class Solution:
    def __init__(self) -> None:
        pass
    
    def insertAtIndex(self, arr,sizeOFArray,index,element):
        if index<0 or index >= sizeOFArray:
            return -1
        arr.insert(index,element)
        return arr

        
        
    
    
if __name__=="__main__":
    g=Solution()
    sizeOfArray = 6
    arr = [1, 2, 3, 4, 5]
    index = 5
    element = 90
    print(g.insertAtIndex(arr,sizeOfArray,index,element))