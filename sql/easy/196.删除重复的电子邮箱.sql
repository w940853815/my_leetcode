--
-- @lc app=leetcode.cn id=196 lang=mysql
--
-- [196] 删除重复的电子邮箱
--
# Write your MySQL query statement below


#思路混乱
-- DELETE FROM Person WHERE Person.Id in (SELECT r.Id FROM (SELECT a.Id FROM Person as a, (SELECT Email,
-- 		COUNT(Email) as num
-- 	FROM
-- 		Person as p

-- 	GROUP BY
-- 		Email
	
-- 	HAVING
-- 		num>1) as b WHERE a.Email=b.Email ORDER BY a.Id LIMIT 1,1000 ) as r)


DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
