-- https://leetcode.com/problems/second-highest-salary/solutions/1168444/summary-five-ways-to-solve-the-top-n-nth-problems/

select max(salary) SecondHighestSalary -- max(salary) to deal with null
from (
    select salary,
        dense_rank() over(order by salary desc) rk from employee
) tmp
where rk=2