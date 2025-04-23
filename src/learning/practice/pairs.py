class pairs:
    def __init__(self) -> None:
        pass
    
    def getPairs(self,arr):
        arr.sort()
        seen=set()
        unique_pairs=set()
        for num in arr:
            complement = -num
            if complement in seen:
                unique_pairs.add(tuple(sorted((num, complement))))
                #unique_pairs.add(tuple(sorted(num, complement)))
            seen.add(num)
        return sorted(unique_pairs)
    
if __name__=="__main__":
    g=pairs()
    print(g.getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))