# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        #reverse the second half
        prev=None
        cur=slow
        while cur is not None:
            newnode=cur.next
            cur.next=prev
            prev=cur
            cur=newnode
        #check palindrome or not
        first=head
        second=prev
        while first and second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True