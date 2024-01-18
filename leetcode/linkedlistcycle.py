# Runtime: 38ms
# Memory: 20.16MB
# Link: https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    getNextNode = lambda node: None if node is None else node.next

    slow_node = head
    fast_node = getNextNode(head)
    while slow_node != fast_node and fast_node != None:
        slow_node = getNextNode(slow_node)
        fast_node = getNextNode(getNextNode(fast_node))
    return fast_node != None
    

        