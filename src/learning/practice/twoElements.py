class twoElements:
    def __init__(self) -> None:
        pass
    
    def findTwoElements(self,arr):
        n=len(arr)
        repeating=-1
        seen=set()
        actual_sum=0
        for num in arr:
            if num in seen:
                repeating=num
            else:
                seen.add(num)
                actual_sum+=num
        expected_sum=n*(n+1)//2
        missing_sum=expected_sum -actual_sum
        return[repeating,missing_sum]
    
if __name__=="__main__":
     g=twoElements()
     print(g.findTwoElements([1, 3, 3]))