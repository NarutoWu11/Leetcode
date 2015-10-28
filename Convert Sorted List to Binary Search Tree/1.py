# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head == None:
            return None
        elif head.next == None:
            return TreeNode(head.val)
        else:
            flag = 0
            fast = slow = head
            while fast and fast.next:
                flag += 1
                slow = slow.next
                fast = fast.next.next
            temp = head
            flag -=1 
            while flag != 0:
                temp = temp.next
                flag -=1
            #temp.next = slow
            temp.next = None
            root = TreeNode(slow.val)
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
            return root