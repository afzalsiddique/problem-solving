WITH cte1 AS -- student count in each department
(
	SELECT department_id
	       ,COUNT(*) cnt
	FROM students
	GROUP BY  1
) 
-- select * from cte1

, cte2 AS
( -- student rank in the dept
	SELECT  s.student_id
          , s.department_id
          , (select cnt from cte1 where s.department_id=department_id) cnt
	       ,rank() over(partition by department_id ORDER BY mark desc) rk
	FROM students s
)
-- select * from cte2

SELECT  student_id
       ,department_id
       ,case when cnt=1 then 0
       else round(
        (rk-1)*100/(cnt-1)
        ,2
       ) 
       end 
       percentage
FROM cte2