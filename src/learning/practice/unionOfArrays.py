class Union:
    def __init__(self) -> None:
        pass
    
    def unionOfArrays(self,arr1,arr2):
        union=set(arr1)|set(arr2)
        return len(union)

if __name__=="__main__":
    g=Union()
    print(g.unionOfArrays([1, 2, 3, 4, 5] , [1, 2, 3]))