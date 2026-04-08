# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        class1=headA
        class2=headB
        while class1 !=class2:
            class1=class1.next if class1 else headB
            class2=class2.next if class2 else headA
        return class2
