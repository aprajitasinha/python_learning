class anagram:
    def __init__(self) -> None:
        pass
    def checkAnangram(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        return  sorted(s1)==sorted(s2)
    
if __name__=="__main__":
    g=anagram()
    print(g.checkAnangram("listen", "silent"))
    print(g.checkAnangram("hello", "world"))