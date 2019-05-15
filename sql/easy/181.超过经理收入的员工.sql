--
-- @lc app=leetcode.cn id=181 lang=mysql
--
-- [181] 超过经理收入的员工
--
# Write your MySQL query statement below
SELECT e1.Name as Employee FROM Employee as e1,Employee as e2 WHERE e1.ManagerId=e2.Id and e1.Salary>e2.Salary

