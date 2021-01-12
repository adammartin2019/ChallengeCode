"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Constraints:

    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

"""

List = [1,2,3,4,5]

def runningSum(nums):
    runningSum = 0
    runSumList = []

    for i in nums:
        runningSum += i
        runSumList.append(runningSum)

        
    print(runSumList)
    return runSumList

runningSum(List)


"""
Complexity analysis

The goal is the running sum of the entire array so the worst case scenario is always the whole array. Only need to
loop through the array once and returns a single array so runtime O(n)



