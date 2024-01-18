# Runtime: 20ms
# Memory: 12.30MB
#Link: https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head:ListNode, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None: return head

        nodes: list[ListNode] = self.getStackOfNodes(head)
        k %= len(nodes) #Cutting a Value if the Number of Rotation excedes len(nodes)
        
        head_pointer = 0; tail_pointer = len(nodes) - 1
        for i in range(k):
            nodes[tail_pointer].next = nodes[head_pointer]
            head_pointer, tail_pointer = tail_pointer, tail_pointer - 1
        nodes[tail_pointer].next = None

        return nodes[head_pointer]

    def getStackOfNodes(self, head:ListNode) -> list:
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
            
        return nodes

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4,ListNode(5)))))
sol = Solution()
answ = sol.rotateRight(node, 2)

while answ != None:
    print(answ.val)
    answ = answ.next