class noOccurance:
    def __init__(self) -> None:
        pass
    def getNoOccurance(self,arr,target):
        count=0
        for i in arr:
            if i==target:
                count+=1
        return count

if __name__=="__main__":
    g=noOccurance()
    print(g.getNoOccurance([1, 1, 2, 2, 2, 2, 3],2))