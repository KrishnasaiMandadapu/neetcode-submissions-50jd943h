# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev

        # Step 1: Reverse
        reverse1 = reverse(head)

        # Step 2: Delete nth from start
        dummy = ListNode(0, reverse1)
        prev = dummy
        curr = reverse1
        count = 1

        while curr:
            if count == n:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1

        # Step 3: Reverse back
        return reverse(dummy.next)
    

        