# solved

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        res = root
        node1 = l1
        node2 = l2
        carry = 0
        while node1 != None or node2 != None or carry != 0:
            val1 = 0 if (node1 == None) else node1.val 
            val2 = 0 if (node2 == None) else node2.val 
            sum = val1 + val2 + carry
            res.val = sum % 10
            carry = sum // 10

            node1 = None if node1 == None else node1.next
            node2 = None if node2 == None else node2.next
            if node1 != None or node2 != None or carry != 0:
                res.next = ListNode()
                res = res.next
        return root
    
