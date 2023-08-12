select s.student_id,s.student_name,sub.subject_name, count(e.student_id) attended_exams
from students s
         cross join Subjects sub
         left join examinations e
                   on s.student_id=e.student_id
                       and sub.subject_name=e.subject_name
group by
    1,2,3
order by
    1,2
;
