# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arrays = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.arrays.append(root.val)
            root = root.right
        self.n = len(self.arrays)
        self.current_pos = -1

    def hasNext(self) -> bool:
        if self.current_pos < self.n-1:
            return True
        return False

    def next(self) -> int:
        self.current_pos += 1
        return self.arrays[self.current_pos]

    def hasPrev(self) -> bool:
        if self.current_pos - 1 >= 0:
            return True
        return False

    def prev(self) -> int:
        self.current_pos -= 1
        return self.arrays[self.current_pos]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()