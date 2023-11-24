with t_max_sal as (
  select company_id
    , max(salary) salary
  from salaries
  group by 1
)
select s.company_id
  , employee_id
  , employee_name
  , round(
  case when mx.salary<1000 then s.salary
  when mx.salary<=10000 then s.salary*0.76
  else s.salary*0.51
  end
  ) salary
from salaries s
join t_max_sal mx
on s.company_id=mx.company_id
