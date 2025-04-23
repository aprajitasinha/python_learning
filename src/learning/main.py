from greet import Greet

g = Greet()
arr = [1, 2, 3, 5]
arr_leader=[16, 17, 4, 3, 5, 2]
arr_duplicate= [2, 3, 1, 2, 3]
arr_eq=[1, 2, 0, 3]
arr_binary = [1, 2, 3, 4, 5]
k = 4
a = [1, 2, 3, 4, 5] 
b = [1, 2, 3]

arr1 = [1, 5, 10, 20, 40, 80] 
arr2 = [6, 7, 20, 80, 100] 
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]




print("Missing Number:", g.missingNumber(arr))
print("Second Largest:", g.getSecondLargest(arr))
print("leaders",g.leaders(arr_leader))
print("duplicate",g.duplicates(arr_duplicate))
print("findEquilibrium",g.findEquilibrium(arr_eq))
print("findTwoElements",g.findTwoElements([1, 3, 3] ))
print("Binaray Search",g.binarySearch(arr_binary,k))
print("Peak Element",g.peakElement(arr))
print("Pair with 0 Sum",g.getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
print("Evenly Divide",g.evenlyDivide(10))
print("Largest Element in Array", g.largestelement(arr_leader))
print("Sum of series",g.sumNaturalNumber(10))
print("SearchArray",g.arraySerach(arr,5))
print("Union Of Array",g.unionOfArrays(a,b))
print("Array Subset",g.araySubset(arr1,arr2))
print("Power of two",g.powerOfTwo(98))
print("Common in 3 Sorted Arrays",)
