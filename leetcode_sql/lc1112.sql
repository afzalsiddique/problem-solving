with highest as (
  select student_id, max(grade) grade
  from enrollments
  group by 1
)
select 
  e1.student_id
  , min(e1.course_id) course_id
  , e1.grade
from enrollments e1
join enrollments e2
on 
-- where # alternative
  (e1.student_id,e1.grade) in (
    select * from highest
  )
group by 1,3
order by 1