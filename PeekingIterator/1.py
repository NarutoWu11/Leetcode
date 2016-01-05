# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = iterator
        self.hasCashe = False
        self.cashe = 0
        if self.nums.hasNext():
            self.hasCashe = True
            self.cashe = iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasCashe:
            return self.cashe
        else:
            return 

    def next(self):
        """
        :rtype: int
        """
        if self.hasCashe:
            return_number = self.cashe
            if self.nums.hasNext():
                self.cashe = self.nums.next()
            else:
                self.hasCashe = False
                self.cashe = 0
            return return_number
        else:
            return 
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.hasCashe:
            return True
        else:
            return False
    
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].