class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        es = [set() for x in range(26)]
        ml = collections.defaultdict(int)
        for w in words:
            num = sum(1 << (ord(x) - ord('a')) for x in set(w))
            ml[num] = max(ml[num], len(w))
            for x in set(string.lowercase) - set(w):
                es[ord(x) - ord('a')].add(num)
        ans = 0
        for w in words:
            r = [es[ord(x) - ord('a')] for x in w]
            if not r: continue
            r = set.intersection(*r)
            for x in r:
                ans = max(ans, len(w) * ml[x])
        return ans