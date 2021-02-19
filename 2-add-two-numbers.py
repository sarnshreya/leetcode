# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""        
        while(l1!=None):
            s1 += str(l1.val) 
            l1 = l1.next
        while(l2!=None):
            s2 += str(l2.val)
            l2 = l2.next
        x = s1[::-1]
        y = s2[::-1]
        res = int(x)+int(y)
        n1 = ListNode()
        begin = n1
        while(res!=0):            
            n1.val = int(res%10)
            res = res//10
            if(res!=0):
                n1.next = ListNode()
                n1 = n1.next
        return begin

