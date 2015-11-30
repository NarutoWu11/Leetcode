class Solution:
	def countNodes(self, root):
		if root == None:
			return 0
		else:
			i = root
			height = 0
			# get the height of the tree
			number = 1
			while i.right!=None:
				i = i.right
				height += 1
			flag = height
			i = root

			# get the height of the rightest node of the tree, just to save the time to 
			# recursively calculate a complete binary tree which has 2^ height nodes in
			# the bottom.
			while i.left != None:
				i = i.left
				flag -=1

			if flag == 0:
				return pow(2, height+1)-1
			else:
				return countNodes(root.left)+countNodes(root.right)+1