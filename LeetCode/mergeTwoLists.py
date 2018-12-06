# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        head = None
        index = None
        if l1.val < l2.val:
            index = l1
            l1 = l1.next
        else:
            index = l2
            l2 = l2.next
        head = index
        while l1 is not None:
            while l2 is not None:
                if l2.val <= l1.val:
                    index.next = ListNode(l2.val)
                    index = index.next
                    l2 = l2.next
                    continue
                else:
                    break
            index.next = ListNode(l1.val)
            index = index.next
            l1 = l1.next

        if l1 is None:
            index.next = l2
        elif l2 is None:
            index.next = l1

        return head


# 1->2->4, 1->3->4
if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    solution = Solution()
    print(solution.mergeTwoLists(l1, l2))
