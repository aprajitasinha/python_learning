from collections import Counter
class Majority:
    def __init__(self) -> None:
        pass
    
    def majorityElement(self, arr,n, x, y):
        count_x=0
        count_y=0
        for i in arr:
            if i==x:
                count_x+=1
            elif i==y:
                count_y+=1
        if count_x>count_y:
            return x
        elif count_y>count_x:
            return y
        else:
            return min(x,y)
        
        
        
        
if __name__=="__main__":
    g=Majority()        
    arr=[1,1,2,2,3,3,4,4,4,4,5]
    n=11
    x=4
    y=5
    print(g.majorityElement(arr,n,x,y)) 
        