class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        a = ['-inf',]
        a.extend(num)
        a.append ('-inf')
        for i in range (1, len(a)-1):
            if float(a[i]) > float(a[i-1]) and float(a[i]) > float(a[i+1]):
                return i-1

if __name__ == '__main__':
    a = Solution()
    print a.findPeakElement([2])