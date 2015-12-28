class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * len(nums)
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            self.sums[i] = sums
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)