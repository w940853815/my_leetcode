--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--
CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
	SET N = N - 1;
	RETURN (
	 SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N, 1
	);
END;

