with allEmployees as (
    select e.employee_id from employees e
        left join salaries s using(employee_id)
    union
    select s.employee_id from employees e
        right join salaries s using(employee_id)
), withInfo as (
    select e.employee_id from employees e
         join salaries s using(employee_id)
)
select a.employee_id from allEmployees a
    left join withInfo w using(employee_id)
where w.employee_id is null
order by 1