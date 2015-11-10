# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def __init__(self):
        self.count = 0
        self.result = 0
    
    def kthSmallest(self, root, k):
        self.count = k
        self.findRightOne(root)
        return self.result
    
    #just the inorder traversal of the tree, minus one when meet the requirements
    def findRightOne(self, root):
        if root.left:
            self.findRightOne(root.left)
        
        #must make sure that when self.count == 0, stop.
        # to prevent there is further change on self.result
        if self.count == 0:
            return
        
        if self.count - 1 == 0:
            self.count = 0
            self.result = root.val
            return
        else:
            self.count -= 1
            if root.right:
                self.findRightOne(root.right)
            else:
                return