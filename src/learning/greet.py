
class Greet:    
    
    @staticmethod
    def missingNumber( arr):
        # code here
        n=len(arr)+1
        total_sum=n*(n+1)//2
        arr_sum=sum(arr)
        return (total_sum-arr_sum)
    
    
    def getSecondLargest( self,arr):
            # Code Here
        if len(arr)<2:
            return -1
        first =float('-inf')
        second= float('-inf')
        for num in arr: 
            if num >first:
                second=first
                first=num
            if num >second and num<first:
                second=num
        return second if second!=float('-inf') else -1
    
    
    def leaders( self,arr):
        # code here
        n=len(arr)
        max_from_right=arr[-1]
        leader=[]
        leader.append(max_from_right)
        for i in range(n-2,-1,-1):
            if arr[i]>=max_from_right:
                max_from_right=arr[i]
                leader.append(max_from_right)
        return leader[::-1]
    
    def duplicates(self,arr):
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
    
    def findEquilibrium(self, arr):
        n=len(arr)
        total_sum=sum(arr)
        left_sum=0
        for i in range(n):
            right_sum=total_sum-left_sum-arr[i]
            if left_sum==right_sum:
                return i
            left_sum+=arr[i]
        return -1
        
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
    
    def binarySearch(self,arr,target):
        for i in range(len(arr)):
            if target==arr[i]:
                return i
        return -1      
     
    def peakElement(self,arr):  
        n=len(arr) 
        for i in range(n):
            left=arr[i-1] if i>0 else float('-inf')  
            right=arr[i+1] if i<n -1 else float('-inf')
            if arr[i]>=left and arr[i]>=right:
                return i
        return -1
    
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
    
    def evenlyDivide(self,n):
        count=0
        for digit in str(n):
            d=int(digit)
            if d!=0 and n%d==0:
                count+=1
        return count
    
    def largestelement(self,arr):
        arr.sort()
        for _ in arr:
            return arr[-1]
        
    def sumNaturalNumber(self,n):
        return n*(n+1)//2
    
    def arraySerach(self,arr,x):
        n=len(arr)
        for i in range(n):
            if arr[i]==x:
                return i
        return -1
    
    def unionOfArrays(self,arr1,arr2):
        union=set(arr1)|set(arr2)
        return len(union)
    
    def araySubset(sef,arr1,arr2):
        freq={}
        for num in arr1:
            freq[num]=freq.get(num,0)+1
        for num in arr2:
            if freq.get(num,0)==0:
                return False
            freq[num]-=1
        return True
    
    def powerOfTwo(self,n):
        if n<=0:
            return False
        return (n&(n-1))==0
        
            
        

            
                
        
            
         
            
                
    
g = Greet()
#print("Returned Missing:", g.missingNumber([[1, 2, 3, 5]]))
#print("Returned Second Largest:", g.getSecondLargest([[1, 2, 3, 5]]))


