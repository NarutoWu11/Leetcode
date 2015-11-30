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
	
	# get the height of the tree
	def getHeight(self, root):
		height = 0
		while root.left:
			height += 1
			root = root.left
		return height
	
	# check if the Kth node of the bottom line is not None
	# the number of the node of the bottom starting from 0 to 2^height - 1.
	# for example. if height = 3. the the node of the bottom starting from 0 ot 7.
	# for the node 0, it should be 000; 1 is 001; 2 is 010; 3 is 011...
	# for 000, it should be left left left; for 001, it should be left left right...
	# so we let k & (height - 1) to see if the result equals to (height - 1), height -= 1
	# then we let k & (height -1 ) to see if the result equals to (height - 1), height -= 1
	# until height == 0
	def getKthNodeonBottomLine(self, root, k, height):
		if k < 0 or k >= (1 << height):
			return None
		while height:
			compareN = 1 << (height - 1)
			# if it equals to compareN, then the corresponding bit of k is 1
			if compareN & k == compareN:
				root = root.right
			else:
				root = root.left
			height -= 1
		return root
	        
