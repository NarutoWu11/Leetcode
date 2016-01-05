# time: O(n), space: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first, second = 0, 0
        vote_for_first, vote_for_second = 0, 0
        results = []
        
        for i in nums:
            if first == i or vote_for_first == 0:
                first = i
                vote_for_first += 1
            elif second == i or vote_for_second == 0:
                second = i
                vote_for_second += 1
            else:
                vote_for_first -= 1
                vote_for_second -= 1
        
        count_first, count_second = 0, 0
        for i in nums:
            if i == first:
                count_first += 1
            elif i == second:
                count_second += 1
                
        if count_first > len(nums)/3: results.append(first)
        if count_second > len(nums)/3: results.append(second)
        
        return results