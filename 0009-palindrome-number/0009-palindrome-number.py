class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        act = x

        while act:
            rev = rev * 10 + act % 10
            act = act // 10

        return rev == x