--
-- @lc app=leetcode.cn id=197 lang=mysql
--
-- [197] 上升的温度
--
# Write your MySQL query statement below


select b.id from Weather as a ,Weather as b where dateDiff(b.RecordDate,a.RecordDate)=1 and a.Temperature < b.Temperature