class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node: ListNode = None

        while head:
            temp: ListNode = head.next
            head.next = node
            node = head
            head = temp

        return node

#T: O(N)
#S: O(1)
