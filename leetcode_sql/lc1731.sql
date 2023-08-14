with a as
(
    select reports_to employee_id,
    count(*) reports_count ,
    round(avg(age),0) average_age
    from employees
    where reports_to is not null
    group by reports_to
)
select e.employee_id, e.name, reports_count,average_age
from employees e
    inner join a
        on a.employee_id=e.employee_id
order by a.employee_id
;
--
select m.employee_id,
	m.name,
	count(*) reports_count ,
	round(avg(e.age),0) average_age
from employees e
	inner join employees m
		on e.reports_to=m.employee_id
group by 1,2
order by 1