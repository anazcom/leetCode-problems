# Runtime: 124 ms
# Memory: 18.08 MB
# Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if head is None: return None
        if self.getNextNode(head) is None: return TreeNode(head.val, None, None)

        before_middle, middle_node = self.getMiddleNodeOfLinkedList(head)
        next_node = self.getNextNode(middle_node)
        before_middle.next = None

        return TreeNode(
            middle_node.val,
            self.sortedListToBST(head),
            self.sortedListToBST(next_node)
        )
    
    def getNextNode(self, node):
        return None if node is None or node.next is None else node.next
    
    def getMiddleNodeOfLinkedList(self, node):
        fast_pointer = self.getNextNode(node)
        slow_pointer = node
        before_slow_pointer = None

        while fast_pointer is not None:
            before_slow_pointer = slow_pointer
            slow_pointer = self.getNextNode(slow_pointer)
            fast_pointer = self.getNextNode(self.getNextNode(fast_pointer))
        
        return (before_slow_pointer, slow_pointer)
    

sol = Solution()
a= sol.sortedListToBST(ListNode(1, ListNode(2, ListNode(3))))