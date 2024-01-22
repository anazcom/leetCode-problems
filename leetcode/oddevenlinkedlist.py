# Runtime: 18 ms
# Memory: 15.20 MB
# Link: https://leetcode.com/problems/odd-even-linked-list

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        getNext = lambda node: None if node is None or node.next is None else node.next
        cloneNode = lambda node: None if node is None else ListNode(node.val)
        
        if head is None or head.next is None: return head
        odd = head; even = getNext(head)
        pointer = even_pointer = even

        while pointer is not None:
            print(f"Odd: {odd.val} Even: {even.val}")
            odd.next = getNext(pointer)
            even.next = getNext(getNext(pointer))

            pointer = even.next
            if odd.next is not None: odd = odd.next
            if even.next is not None: even = even.next
        odd.next = even_pointer

        return head



sol = Solution()
#[1,2,3,4,5]
sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print("=================")
#[1,2,3,4,5,6,7,8]
sol.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))))