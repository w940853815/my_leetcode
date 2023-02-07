#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#
from typing import List
import datetime
from collections import defaultdict
# @lc code=start
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_time = defaultdict(list)
        alter_names=[]
        for name,time in zip(keyName,keyTime):        
            name_time[name].append(time)
        for key,val in name_time.items():
            val.sort()
            if any((datetime.datetime.strptime(time2,"%H:%M")-datetime.datetime.strptime(time1,"%H:%M")).seconds / 60 /60<=1 for time1,time2 in zip(val,val[2:])):
                alter_names.append(key)
        alter_names.sort()
        return alter_names

# @lc code=end

if __name__=='__main__':
    s=Solution()
    res=s.alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"],["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])
    print(res)
    res=s.alertNames(["a","a","a","a","a","a","b","b","b","b","b"],["23:27","03:14","12:57","13:35","13:18","21:58","22:39","10:49","19:37","14:14","10:41"])
    # ["a"]
    print(res)
    res=s.alertNames(["alice","alice","alice","bob","bob","bob","bob"],["12:01","12:00","18:00","21:00","21:20","21:30","23:00"])
    # ["bob"]
    print(res)
    res=s.alertNames(["john","john","john"],["23:58","23:59","00:01"])
    # []
    print(res)