# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        maximum=0
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        
        #revverse the second one
        prev=None
        cur=slow
        while cur is not None:
            newnode=cur.next
            cur.next=prev
            prev=cur
            cur=newnode
        #find the maximum
        first=head
        while first and prev:
            value=first.val+prev.val
            maximum=max(maximum,value)
            first=first.next
            prev=prev.next
        return maximum


        
        