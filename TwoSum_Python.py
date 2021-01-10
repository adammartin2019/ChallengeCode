NUMS = [2,7,11,15]
TARGET = 9

"""
Brute force method check each pair of numbers linarly in the array. Results in O(n^2) runtime
def twoSum(nums, target):
    indexList = []
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            b = nums[j]
            sum = a+b
            if sum == target:
                indexList.append(i)
                indexList.append(j)
                print(indexList)
                return indexList

twoSum(NUMS, 9)
"""

"""
This runs in O(n) because the dict/ hashmap reduces lookup time to O(1) and we only need a single pass 
through the input array

#Two pass hash table
def twoSum(nums, target):
    indexList = []
    hMap = {}

    for i in range(len(nums)):
        hMap.update({nums[i]:i})
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hMap and hMap.get(complement) != i:
            indexList.append(i)
            indexList.append(hMap.get(complement))
            print(indexList)
            return indexList
    
            
twoSum([2,7,11,15], 9)

"""

#The best solution combines hash table insertion and checking the complement at the same time
#resulting in O(n) runtime as well as space complexity

    