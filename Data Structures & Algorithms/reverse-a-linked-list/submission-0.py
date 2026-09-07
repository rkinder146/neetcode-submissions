# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        def reverseListHelp(curr):
            if curr.next is None:
                head = curr
                return (curr, curr);
            
            temp = reverseListHelp(curr.next)
            next = temp[0]
            next.next = curr
            curr.next = None
            return (curr, temp[1])
        
        return reverseListHelp(head)[1]
        