with max_sal as (
    select d.id, max(e.salary) max_sal from department d
        join employee e on d.id=e.departmentid
    group by 1
)
select d.name Department,e.name Employee,e.salary Salary from department d
    join employee e on d.id=e.departmentid
    where (e.departmentid, e.salary) in (select * from max_sal)
    