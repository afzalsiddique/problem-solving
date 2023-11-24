
select max(salary) SecondHighestSalary
from (
    select salary,
        dense_rank() over(order by salary desc) rk from employee
) tmp
where rk=2