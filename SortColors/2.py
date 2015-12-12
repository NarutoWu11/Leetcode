class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = -1
        blue = len(A)
        i = 0
        #attention: in this way, can be i< blue, since we initiate different blue and red's value
        while i < blue:
          if A[i] == 0:
            red += 1
            A[i], A[red] = A[red], A[i]
            i += 1
            #red += 1
          elif A[i] == 1:
            i += 1
          else:
            blue -= 1
            A[i], A[blue] = A[blue], A[i]
