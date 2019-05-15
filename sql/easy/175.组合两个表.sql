--
-- @lc app=leetcode.cn id=175 lang=mysql
--
-- [175] 组合两个表
--
# Write your MySQL query statement below

select Salary  as SecondHighestSalary from Employee  order by SecondHighestSalary desc  LIMIT 1 offset 1;
