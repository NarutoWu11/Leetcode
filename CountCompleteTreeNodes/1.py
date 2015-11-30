#TLE

class Solution:
	
	def countNodes(self, root):
		if root == None:
			return 0
		else:
			number = 1
			queueofnodes = []
			queueofnodes.append(root)
			head = 0
			while head < len(queueofnodes):
				if queueofnodes[head].left == None:
					return number
				else:
					number += 1
					if queueofnodes[head].right == None:
						return number
					else:
						number +=1
						queueofnodes.append(queueofnodes[head].left)
						queueofnodes.append(queueofnodes[head].right)
						head +=1
class TreeNode:
    def __init__(self, x):
    	self.val = x
    	self.left = None
    	self.right = None

if __name__ == "__main__":
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	d=TreeNode(3)
	b.left=d
	a.left=b
	a.right=c
	d = Solution()
	print d.countNodes(a)