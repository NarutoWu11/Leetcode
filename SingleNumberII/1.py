class Solution:
    # @param num, a list of integers
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        i = 0
        record = 1
        while (i < (len(A) -1)):
            if A[i] == A[i+1]:
                record += 1
                i += 1
                continue
            else:
                if record == 3:
                    record = 1
                    i += 1
                else:
                    return A[i]
        return A[i]

if __name__ == "__main__":
	a = Solution()

	print a.singleNumber([1])