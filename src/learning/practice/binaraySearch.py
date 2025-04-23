class binarySearch:
    def __init__(self) -> None:
        pass
    
    def getBinarySearch(self,arr,target):
            for i in range(len(arr)):
                if target==arr[i]:
                    return i
            return -1      


if __name__=="__main__":
    g=binarySearch()
    print(g.getBinarySearch([1, 2, 3, 4, 5],4))