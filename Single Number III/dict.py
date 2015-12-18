class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        dict_singleNumber = {}
        results = []
        for i in nums:
            if i not in dict_singleNumber:
                dict_singleNumber[i] = 1
            else:
                dict_singleNumber[i] += 1
        
        for i in dict_singleNumber:
            if dict_singleNumber[i] != 2:
                results.append(i)
        
        return results
        