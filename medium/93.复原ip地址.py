#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if (a + b + c + d) == len(s):
                            ip1 = int(s[0:a])
                            ip2 = int(s[a: a + b])
                            ip3 = int(s[a + b: a + b + c])
                            ip4 = int(s[a + b + c:])
                            if ip1 <= 255 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
                                ip = '.'.join(
                                    [str(ip1), str(ip2), str(ip3), str(ip4)])
                                if len(ip) == len(s) + 3:
                                    res.append(ip)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.restoreIpAddresses("010010")
    print(res)
# @lc code=end
