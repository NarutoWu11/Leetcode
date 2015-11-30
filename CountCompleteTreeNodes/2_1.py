class Solution:
	def countNodes(self, root):
		if not root:
			return 0
		else:
			height = self.getHeight(root)
			left, right = 0, (1 << height) - 1
			while left <= right:
				mid = (left + right ) >> 1
				if self.getKthNodeonBottomLine(root, mid, height):
					left = mid + 1
				else:
					right = mid - 1        
			return (left + (1 << height), right + (1 << height))[self.getKthNodeonBottomLine(root, right, height)!=None]
	
	def getHeight(self, root):
		height = 0
		while root.left:
			height += 1
			root = root.left
		return height
	
	def getKthNodeonBottomLine(self, root, k, height):
		if k < 0 or k >= (1 << height):
			return None
		while height:
			compareN = 1 << (height - 1)
			if compareN & k == compareN:
				root = root.right
			else:
				root = root.left
			height -= 1
		return root
	        
	        