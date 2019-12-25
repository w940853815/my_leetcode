#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # init
        # Time Limit Exceeded
        # max_len = 1000
        # res = [[None for j in range(max_len)] for i in range(numRows)]
        # s_list = [i for i in s[::-1]]
        # x = 0
        # while s_list:
        #     y = 0
        #     for i in range(numRows):
        #         if not s_list:
        #             break
        #         res[y][x] = s_list.pop()
        #         y += 1
        #     y -= 1
        #     for i in range(numRows - 2):
        #         x += 1
        #         y -= 1
        #         if not s_list:
        #             break
        #         res[y][x] = s_list.pop()
        #     x += 1
        # string = ''
        # for i in range(len(res)):
        #     for j in range(len(res[i])):
        #         if res[i][j] != None:
        #             string += res[i][j]
        # return string
        if numRows == 1:
            return s
        rows = [''] * min(numRows, len(s))
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        res = ''.join(rows)
        return res


if __name__ == "__main__":
    # ['', '', '']
    # ['L', '', '']
    # ['L', 'E', '']
    # ['L', 'E', 'E']
    # ['L', 'ET', 'E']
    # ['LC', 'ET', 'E']
    # ['LC', 'ETO', 'E']
    # ['LC', 'ETO', 'ED']
    # ['LC', 'ETOE', 'ED']
    # ['LCI', 'ETOE', 'ED']
    # ['LCI', 'ETOES', 'ED']
    # ['LCI', 'ETOES', 'EDH']
    # ['LCI', 'ETOESI', 'EDH']
    # ['LCIR', 'ETOESI', 'EDH']
    # ['LCIR', 'ETOESII', 'EDH']
    # ['LCIR', 'ETOESII', 'EDHN']
    # ['LCIR', 'ETOESIIG', 'EDHN']
    # LCIRETOESIIGEDHN
    s = Solution()
    res = s.convert("LEETCODEISHIRING", 3)
    print(res)
# @lc code=end
