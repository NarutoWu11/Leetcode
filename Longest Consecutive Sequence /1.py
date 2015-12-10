class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        diction = {}
        longest = 1
        for i in nums:
            diction[i] = 1
        for i in nums:
            if diction[i] != 1:
                continue
            else:
                length = 1
                temp = i-1
                while diction.has_key(temp):
                    length += 1
                    diction[temp] = length
                    temp -=1
                temp = i+1
                while diction.has_key(temp):
                    length += 1
                    diction[temp] = length
                    temp +=1
                diction[i] = length
                longest = max(longest, length)
        return longest