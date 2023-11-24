with base_table as (
SELECT  left( pay_date ,7) pay_month
       ,e.department_id
       ,amount
FROM salary s
JOIN employee e
ON s.employee_id = e.employee_id
)
-- select * from base_table
, comp_avg as (
  select pay_month
    , avg(amount) amount
  from base_table
  group by 1
)
-- select * from comp_avg
select b.pay_month
  , department_id
  -- , round(avg(b.amount),2) dept_avg
  -- , round(avg(c.amount),2) company_avg
  , case 
  when round(avg(b.amount),2)>round(c.amount,2) then 'higher'
  when round(avg(b.amount),2)<round(c.amount,2) then 'lower'
  else 'same'
  end comparison
from base_table b
join comp_avg c
on b.pay_month=c.pay_month
group by 1,2