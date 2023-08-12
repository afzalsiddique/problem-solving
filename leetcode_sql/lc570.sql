select e2.name
from employee e1
    inner join employee e2
        on e1.managerId=e2.id
group by e1.managerid
having count(e1.managerid)>=5;