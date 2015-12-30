import string

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #use es to record the word which doesn't contain corresponding letter
        #for example, es[0] is the set of number which doesn't have 'a'
        except_letter = [set() for x in range(26)]
        
        #use dict word_length to record the longest word which has the same number
        word_length = {}
        
        for word in words:
            num_word = sum(1 << (ord(x) - ord('a')) for x in set(word))
            
            # update it to the dict
            if num_word not in word_length:
                word_length[num_word] = len(word)
            else:
                word_length[num_word] = max(len(word), word_length[num_word])
                
            # add num_word to the corresponding except_letter which word doesn't contain the letters
            for letter in set(string.lowercase)-set(word):
                except_letter[(ord(letter) - ord('a'))].add(num_word)
        
        Maximum_product = 0
        
        for word in words:
            legit_words = [except_letter[ord(letter)- ord('a')] for letter in set(word)]
            
            if not legit_words:
                continue
            
            # get the intersection of the 
            intersection_words = legit_words[0]
            for each_set in legit_words:
                intersection_words = intersection_words.intersection(each_set)
            
            for i in intersection_words:
                Maximum_product = max(Maximum_product, word_length[i] * len(word))
        
        
        
        return Maximum_product