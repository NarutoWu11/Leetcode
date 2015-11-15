class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
    	goal = ''
        a = s.split(' ')
        for i in range(len(a)-1, -1, -1):
            if len(a[i]) > 0:
                goal += a[i]
                goal += ' '
            else:
                continue
        #delete the last ' '
        goal = goal[0:len(goal)-1]
        return goal

if __name__ == "__main__":
	a = Solution()
	print a.reverseWords('     the sky is    blue  ')