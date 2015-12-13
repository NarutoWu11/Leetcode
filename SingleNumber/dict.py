class Solution:
    def singleNumber(self, A):
        dict_number = {}
        for i in A:
            if i not in dict_number:
                dict_number[i] = 1
            else:
                dict_number[i] += 1
        for i in dict_number:
            if dict_number[i] == 1:
                return i