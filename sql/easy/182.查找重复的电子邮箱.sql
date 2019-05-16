--
-- @lc app=leetcode.cn id=182 lang=mysql
--
-- [182] 查找重复的电子邮箱
--
# Write your MySQL query statement below
SELECT Email FROM (SELECT Email,COUNT(Email) as count FROM Person GROUP BY Email) as p WHERE count >1; 
