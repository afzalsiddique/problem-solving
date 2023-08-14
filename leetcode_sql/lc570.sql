select manager.name
from employee
    inner join employee manager
        on employee.managerId=manager.id
group by employee.managerid
having count(employee.managerid)>=5;