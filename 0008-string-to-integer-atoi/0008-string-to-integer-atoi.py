class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)

        res = 0
        is_neg = False

        s = s.lstrip()

        if s and s[0] in ['-', '+']:
            if s[0] == '-':
                is_neg = True
            s = s[1:]
        for i in s:
            if i.isdigit():
                res = res * 10 + int(i)
                if not is_neg and res > INT_MAX:
                    return INT_MAX
                elif is_neg and -res < INT_MIN:
                    return INT_MIN
            else:
                break

        if res != 0 and is_neg:
            res = -res

        return res