# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count = 0
        current = root
        while current:
            count += 1
            current = current.next
        width, remainder = divmod(count, k)
        print(width, remainder)
        ans = []
        current = root
        for i in range(k):
            head = current
            if i < remainder:
                for _ in range(width):
                    if current:
                        current = current.next
            else:
                for _ in range(width - 1):
                    if current:
                        current = current.next
            if current:
                current.next, current = None, current.next
            ans.append(head)
        return ans
                