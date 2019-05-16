--
-- @lc app=leetcode.cn id=183 lang=mysql
--
-- [183] 从不订购的客户
--
# Write your MySQL query statement below

-- SELECT Name as Customers FROM (select c.Id as cid,c.Name,o.Id as oid
-- 	from
-- 		Customers as c LEFT JOIN
-- 		Orders as o
-- 	ON
-- 		c.Id = o.CustomerId) as tmp WHERE oid is NULL

-- SELECT Name FROM Customers as c LEFT JOIN Orders as o ON c.Id=o.CustomerId WHERE o.CustomerId is NULL

SELECT Name FROM Customers WHERE Id NOT IN(SELECT CustomerId FROM Orders)
