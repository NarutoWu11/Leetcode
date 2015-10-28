class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        else:
            slow, fast = head, head
            temp = None
            while fast!=None and fast.next!=None:
                temp = slow
                slow = slow.next
                fast = fast.next.next
            temp.next = None
            root = TreeNode(slow.val)
            left_child = self.sortedListToBST(head)
            right_child = self.sortedListToBST(slow.next)
            root.left = left_child
            root.right = right_child
            return root