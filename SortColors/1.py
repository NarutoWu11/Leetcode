class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = 0
        blue = len(A) - 1
        i = 0
        #attention: i<=blue not i<blue. if i < blue, then may not traverse all the colors
        while i <= blue:
          if A[i] == 0:
            A[i], A[red] = A[red], A[i]
            i += 1
            red += 1
          elif A[i] == 1:
            i += 1
          else:
            A[i], A[blue] = A[blue], A[i]
            blue -= 1




