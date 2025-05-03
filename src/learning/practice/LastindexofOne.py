class Solution:
    def __init__(self):
        pass
    
    def lastIndexOfOne(self,s):
        if not s:
            return -1
        last_index = -1
        for i in range(len(s)):
            if s[i] == '1':
                last_index = i
        return last_index

if __name__=="__main__":
    g=Solution()
    arr="00001"
    print(g.lastIndexOfOne(arr))