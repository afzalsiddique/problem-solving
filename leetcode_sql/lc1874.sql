with t0 as (
  select salary
  , dense_rank() over(order by salary) team_id
  from employees
  group by salary
  having count(*)>1
)
select employee_id,name,t0.salary,t0.team_id
from employees e
join t0
on e.salary=t0.salary
order by 4,1