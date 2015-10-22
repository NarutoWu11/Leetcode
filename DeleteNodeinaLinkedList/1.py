# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node.next!= None:
        	# do not know why node = node.next is wrong
            node.val = node.next.val
            node.next = node.next.next
        return