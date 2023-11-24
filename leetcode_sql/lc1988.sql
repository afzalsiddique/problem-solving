with cte as (
  SELECT  s.school_id
        -- ,s.capacity
        ,(
            SELECT 
              max(student_count)
            from exam 
            where student_count<=s.capacity
              ) student_count
  FROM schools s
)
select cte.school_id
    , min(e.score) score
from cte
join exam e
on e.student_count=cte.student_count
group by 1
union
select school_id
  , -1 score
from cte
where student_count is null