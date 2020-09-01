class Solution:
	def find_predecessor(self, root):
		root = root.left
		while root.right:
			root = root.right
		return root.val


	def find_successor(self, root):
		root = root.right
		while root.left:
			root = root.left
		return root.val

	def deleteNode(self, root, key):
		if not root:
			return None
		elif root.val > key:
			root.left = self.deleteNode(root.left, key)
		elif root.val < key:
			root.right = self.deleteNode(root.right, key)
		else:
			if not(root.left or root.rigth):
				return None
			elif root.left:
				root.val = self.find_predecessor(root)
				root.left = self.deleteNode(root.left, root.val)
			else:
				root.val = self.find_successor(root)
				root.right = self.deleteNode(root.right, root.val)
		return root