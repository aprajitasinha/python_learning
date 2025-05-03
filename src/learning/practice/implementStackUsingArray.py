class MyStack:
    def __init__(self) -> None:
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
        
    
    
def self_query(queries): 
    s=MyStack()
    result=[]
    i=0
    while i<len(queries):
        if queries[i]=="1":
            i+=1
            s.push(int(queries[i]))
        elif queries[i]=="2":
            popped=s.pop()
            if popped!=-1:
                result.append(str(popped))
        i+=1
    print(" ".join(result))
    
if __name__=="__main__":
    queries = ["1", "2", "3", "4", "2", "1", "5", "2"]
    self_query(queries)
        
            
            
       
    
        
        