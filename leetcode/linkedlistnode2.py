#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        getNext = lambda node: None if node is None or node.next is None else node.next

        slow_node = head
        fast_node = head

        while True:
            slow_node = getNext(slow_node)
            fast_node = getNext(getNext(fast_node))

            if fast_node == None or slow_node == fast_node: break

        if fast_node is None: return "no cycle"

        slow_node = head
        pos = 0
        while slow_node != fast_node:
            slow_node = getNext(slow_node)
            fast_node = getNext(fast_node)
            pos += 1   

        return f"tail connects to node index {pos}"


sol = Solution()
assert sol.detectCycle(ListNode(1)) == "no cycle"
assert sol.detectCycle(l)
