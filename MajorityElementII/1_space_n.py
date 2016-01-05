class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        times = len(nums)/3
        dict_num = {}
        results = []
        for i in nums:
            if i in dict_num:
                dict_num[i] += 1
            else:
                dict_num[i] = 1
        
        
        for i in dict_num:
            if dict_num[i] > times:
                results.append(i)
        return results