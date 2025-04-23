class duplicates:
    def __init__(self) -> None:
        pass
    
    def get_duplicates(self,arr):
        freq_map={}
        duplicates=[]
        for num in arr:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1
        for key, value in freq_map.items():
            if value >1:
                duplicates.append(key)
        return duplicates
    
if __name__=="__main__":
    g=duplicates()
    print(g.get_duplicates([2, 3, 1, 2, 3]))
    