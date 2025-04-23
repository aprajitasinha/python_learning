class common:
    def __init__(self) -> None:
        pass
    
    def commonOfArray(self,arr1,arr2,arr3):
        s1=set(arr1)
        s2=set(arr2)
        s3=set(arr3)
        common=s1&s2&s3
        return sorted(common) if common else -1

if __name__=="__main__":
    g=common()
    print(g.commonOfArray([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))
    
    