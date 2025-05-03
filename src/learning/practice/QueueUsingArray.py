class MyQueue:
    def __init__(self) -> None:
        self.queue = []
    
    def push(self,x):
        self.queue.append(x)
    
    def pop(self):
        if len(self.queue)==0:
            return -1
        return self.queue.pop(0)



def self_query(queries):
    s=MyQueue()
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
    input_str = "1 2 1 3 2 1 4 2"
    queries = input_str.strip().split()
    self_query(queries)

    
    