# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stackofnodes = []
        temp = root
        
        while temp or stackofnodes:
            if temp!= None:
                stackofnodes.append(temp)
                temp = temp.left
            else:
                temp = stackofnodes.pop()
                k -= 1
                if k == 0:
                    return temp.val
                else:
                    temp = temp.right