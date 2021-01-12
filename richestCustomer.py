"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has 
the maximum wealth.

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Constraints:

    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100


"""

accounts = [[2,8,7],[7,1,3],[1,9,5]]     

def maximumWealth(accounts):
    accountSums = []

    for i in accounts:
        SUM=0
        for j in range(len(i)):
            SUM += i[j]
        accountSums.append(SUM)
    print(max(accountSums))
    return max(accountSums)

maximumWealth(accounts)


"""
Complexity Analysis

The problem is constrained to size 50 so the algorithm doesn't need to be super efficient to be relatively fast.
This is another example where every value needs to be checked in a 2d array so a nested for loop is necessary.
Since we traverse every element in every array the runtime is O(N*M)

Another solution
def maximumWealth(accounts):
		listOfSums = []
		for a in accounts:
			listOfSums.append(sum(a))
		maxSum = max(listOfSums)
		return maxSum
