select dept_name
	, coalesce(count(s.student_id),0) student_number
from department d
left join student s
on s.dept_id=d.dept_id
group by d.dept_id
order by 2 desc,1