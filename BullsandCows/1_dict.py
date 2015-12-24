class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dict_secret = {}
        dict_guess = {}
        number_of_bulls = 0
        number_of_cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                number_of_bulls += 1
            else:
                if secret[i] not in dict_secret:
                    dict_secret[secret[i]] = 1
                else:
                    dict_secret[secret[i]] +=1
                if guess[i] not in dict_guess:
                    dict_guess[guess[i]] = 1
                else:
                    dict_guess[guess[i]] += 1
        
        for i in dict_secret:
            if i in dict_guess:
                number_of_cows += min(dict_secret[i], dict_guess[i])
        
        return str(number_of_bulls)+"A"+str(number_of_cows)+"B"