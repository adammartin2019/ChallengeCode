"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


"""

#This solution ignores the linked list aspect, not correct for the given problem
l1 = [2,4,3]
l2 = [5,6,4]

L1 = [0]
L2 = [0]

LIST1 = [9,9,9,9,9,9,9]
LIST2 = [9,9,9,9]

def addTwoNumbers(l1, l2):
    L1r = []
    L2r = []
    for i in reversed(l1):
        L1r.append(i)

    for j in reversed(l2):
        L2r.append(j)

    num1 = int(''.join(map(str,L1r)))
    num2 = int(''.join(map(str,L2r)))

    addNum = num1 + num2 

    finalNumList = [int(i) for i in reversed(str(addNum))]
    print(finalNumList)

    return finalNumList

addTwoNumbers(l1,l2)
addTwoNumbers(L1,L2)
addTwoNumbers(LIST1,LIST2)


    


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node: 
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def listPrint(self):
        printVal = self.headval
        while printVal is not None:
            print(printVal.dataval)
            printVal = printVal.nextval

L1 = LinkedList()
L2 = LinkedList()

#generate list 1
L1.headval = Node(2)
l1n2 = Node(4)
l1n3 = Node(3)

L1.headval.nextval = l1n2
l1n2.nextval = l1n3

#generate list 2
L2.headval = Node(5)
l2n2 = Node(6)
l2n3 = Node(4)

L2.headval.nextval = l2n2
l2n2.nextval = l2n3

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """ 
    result = Node(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.dataval if l1 else 0)
        val2  = (l2.dataval if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                    
        result_tail.nextval = Node(out)
        result_tail = result_tail.nextval                     
        
        l1 = (l1.nextval if l1 else None)
        l2 = (l2.nextval if l2 else None)

    return result.nextval

addTwoNumbers(L1.headval, L2.headval)

"""
Intuition

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, 
which contains the least-significant digit.

Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, 
which is the head of l1l1l1 and l2l2l2. Since each digit is in the range of 0…90 \ldots 90…9, summing two digits 
may "overflow". For example 5+7=125 + 7 = 125+7=12. In this case, we set the current digit to 222 and bring over 
the carry=1carry = 1carry=1 to the next iteration. carrycarrycarry must be either 000 or 111 because the largest 
possible sum of two digits (including the carry) is 9+9+1=199 + 9 + 1 = 199+9+1=19.

The pseudocode is as following:

    Initialize current node to dummy head of the returning list.
    Initialize carry to 000.
    Initialize ppp and qqq to head of l1l1l1 and l2l2l2 respectively.
    Loop through lists l1l1l1 and l2l2l2 until you reach both ends.
        Set xxx to node ppp's value. If ppp has reached the end of l1l1l1, set to 000.
        Set yyy to node qqq's value. If qqq has reached the end of l2l2l2, set to 000.
        Set sum=x+y+carrysum = x + y + carrysum=x+y+carry.
        Update carry=sum/10carry = sum / 10carry=sum/10.
        Create a new node with the digit value of (sum mod 10)(sum \bmod 10)(summod10) and set it to current node's next, 
            then advance current node to next.
        Advance both ppp and qqq.
    Check if carry=1carry = 1carry=1, if so append a new node with digit 111 to the returning list.
    Return dummy head's next node.

Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements 
to initialize the head's value.

Complexity Analysis

    Time complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). Assume that mmm and nnn represents the length of l1l1l1 and l2l2l2 
    respectively, the algorithm above iterates at most max⁡(m,n)\max(m, n)max(m,n) times.

    Space complexity : O(max⁡(m,n))O(\max(m, n))O(max(m,n)). The length of the new list is at most 
    max⁡(m,n)+1\max(m,n) + 1max(m,n)+1.


"""

