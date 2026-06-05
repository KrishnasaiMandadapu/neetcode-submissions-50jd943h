# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        def reverse(head: Optional[ListNode])-> Optional[ListNode]:
            curr=head
            prev=None
            while curr:
                nextNode=curr.next
                curr.next=prev

                prev=curr
                curr=nextNode
            return prev

        reverse1=reverse(head)
        dummy=ListNode(0,reverse1)

        temp1= dummy
        cnt=1

        while temp1:

            if cnt==n:
                temp1.next=temp1.next.next 
            
            cnt+=1
            temp1=temp1.next

        reverse2=reverse(dummy.next)

        return reverse2
    

        