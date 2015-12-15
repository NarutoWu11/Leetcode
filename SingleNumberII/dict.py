class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dict_singleNumber = {}
        for i in A:
            if i not in dict_singleNumber:
                dict_singleNumber[i] = 1
            else:
                dict_singleNumber[i] += 1
        for i in dict_singleNumber:
            if dict_singleNumber[i] != 3:
                return i