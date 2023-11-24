with exam_student as (
  select distinct student_id from exam
)
, max_min_score(exam_id,score) as (
  select exam_id
    , max(score)
  from exam
  group by 1
  union
  select exam_id
    , min(score)
  from exam
  group by 1
)
, max_min_student as (
  select distinct e.student_id
  from exam e
  join max_min_score m
  on e.exam_id=m.exam_id and e.score=m.score
)
select s.student_id
  , s.student_name
from student s
join exam_student e
on s.student_id=e.student_id
where s.student_id not in (select * from max_min_student)
order by 1