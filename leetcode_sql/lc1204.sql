select person_name from (
    select person_name,
        sum(weight) over(order by turn) as grossWeight
    from queue) weightTable
where grossWeight<=1000
order by grossWeight desc
limit 1
;
