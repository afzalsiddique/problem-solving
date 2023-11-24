with employee_count as (
  select company
    , count(*) cnt
  from employee
  group by 1
)
, median as (
  select distinct company
    , ceil(cnt/2) median_row
  from employee_count
  union
  select distinct company
    , ceil((cnt+1)/2) median_row
  from employee_count
)
-- select * from median
, salary_rank as (
  select *
    , rank() over(partition by company order by salary,id) rk
  from employee
)
select id
  , sr.company
  , sr.salary
 from salary_rank sr
 join median m
 on sr.company=m.company
 where rk=m.median_row