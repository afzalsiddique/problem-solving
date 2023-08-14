-- window
with weightTable as (
    select person_name,
           sum(weight) over(order by turn) as grossWeight
    from queue)
select person_name
from weightTable
where grossWeight<=1000
order by grossWeight desc
    limit 1
;
-- join
SELECT q1.person_name
FROM Queue q1
    JOIN Queue q2
        ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1