
WITH cte AS
(
	SELECT  departmentid
	       ,salary
	       ,dense_rank() over(partition by departmentid ORDER BY salary desc) rk
	FROM employee
) , cte2 AS
(
	SELECT  distinct departmentid
	       ,salary
	FROM cte
	WHERE rk <= 3 
)
SELECT  
       d.name department
       ,e.name employee
       ,e.salary
FROM employee e
JOIN cte2
ON e.departmentid = cte2.departmentid AND e.salary = cte2.salary
join department d
on d.id=e.departmentid