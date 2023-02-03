#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
from typing import List
# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        new_strs =[]
        for i in range(len(strs[0])):
            tmp = ''
            for s in strs:
                tmp+=s[i]
            new_strs.append(tmp)
        res = 0
        for ns in new_strs:
            for i in range(1,len(ns)):
                if ns[i-1]>ns[i]:
                    res+=1
                    break
        return res
# @lc code=end
if __name__=='__main__':
    s=Solution()
    res=s.minDeletionSize(["cba","daf","ghi"])
    print(res)
    res=s.minDeletionSize(["a","b"])
    print(res)
    res=s.minDeletionSize(["zyx","wvu","tsr"])
    print(res)

