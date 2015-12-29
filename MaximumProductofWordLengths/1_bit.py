class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_bit = [0] * len(words)
        for i in range(len(words)):
            words_bit[i] = sum( 1 << ord(x) - ord('a') for x in set(words[i]))
        
        max_product = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words_bit[i] & words_bit[j] == 0:
                    max_product = max(len(words[i]) * len(words[j]), max_product)
        return max_product