class Solution(object):
    def isPalindrome(self, x):
        result = True
        if type(x) != int or x < 0:
            result = False
            return result
        length = len(str(x))
        for i in range(0, length / 2):
            if (x / (10 ** i) - (x / (10 ** (i +1))) * 10) != (x / 10 ** (length - 1 -i) - (x / (10 ** (length - i))) * 10):
                result = False
                break
        return result
