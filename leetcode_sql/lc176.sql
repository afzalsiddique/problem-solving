-- subquery 1
select max(salary) SecondHighestSalary
from employee
where salary not in (select max(salary) from employee)
-- order by limit offset
SELECT(SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
          LIMIT 1 OFFSET 1)
    AS SecondHighestSalary;
-- ifnull
SELECT IFNULL(
               (SELECT DISTINCT salary
                FROM employee
                ORDER BY salary DESC
                   LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;
