class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        cur = 0
        direction = 'UP'

        for i in s:
            res[cur].append(i)
        
            if direction == 'UP':
                if cur == numRows - 1:
                    direction = 'DOWN'
                    cur -= 1
                    cur = max(cur, 0)
                else:
                    cur += 1
                    cur = min(cur, numRows - 1)
            else:
                if cur == 0:
                    direction = 'UP'
                    cur += 1
                    cur = min(cur, numRows - 1)
                else:
                    cur -= 1
                    cur = max(cur, 0)
        temp = []
        for x in res:
            temp.append("".join(x))
        return "".join(temp)