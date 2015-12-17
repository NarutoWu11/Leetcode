class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        diff = 0
        for i in nums:
            diff ^= i
        diff &= -diff
        a= []
        b= []
        for i in nums:
            if diff & i:
                a.append(i)
            else:
                b.append(i)
        ans = []
        j = 0
        for i in a:
            j ^= i
        ans.append(j)
        j = 0
        for i in b:
            j ^= i
        ans.append(j)
        return ans