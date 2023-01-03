#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = ""
        num_list = []
        s += " "
        for i in s:
            if i.isdigit():
                num += i
            else:
                if num:
                    num_list.append(int(num))
                    num = ""
        return sorted(num_list) == num_list and len(set(num_list)) == len(num_list)


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    print(res)
    res = s.areNumbersAscending("hello world 5 x 5")
    print(res)
