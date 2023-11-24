WITH work AS
(
	SELECT  employee_id
	       ,SUM( round(timestampdiff(second,in_time ,out_time)/60+0.5,0) ) duration
	FROM logs
	GROUP BY  1
)
SELECT  e.employee_id
FROM employees e
LEFT JOIN work w
ON e.employee_id = w.employee_id
-- use coalesce to include employee ids which do not have any records in the logs table
WHERE coalesce(duration, 0) < needed_hours*60 