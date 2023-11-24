select 
  distinct candidate_id 
from Candidates c
join rounds r
on c.interview_id=r.interview_id
where c.years_of_exp>=2
group by r.interview_id
having sum(score)>15