class Solution:
    def __init__(self):
        pass
    
    def removeDuplicates(self,s):
        seen=set()
        result=[]   
        for char in s:
            if  char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)              
            
    
    
if __name__=="__main__":
   g=Solution() 
   print(g.removeDuplicates("geEksforGEeks"))
            