-- 1 full join (mySQL doesnt have full join. so combine left and right join)
select T.employee_id from(
    select * from employees as E right join
         salaries as S using(employee_id)
    union
    select * from employees as E left join
          salaries as S using(employee_id)
    )
as T
where T.name is null or T.salary is null
ORDER BY employee_id ;

-- 2 union and not in
select employee_id from employees
    where employee_id not in (select distinct employee_id from salaries)
union
select employee_id from salaries
    where employee_id not in (select distinct employee_id from employees)
order by employee_id;

-- 3 union and not exists
select employee_id from employees as E
    where not exists (select distinct employee_id from salaries as S where S.employee_id=E.employee_id)
union
select employee_id from salaries as S
    where not exists (select distinct employee_id from employees as E where S.employee_id=E.employee_id)
order by employee_id;
