with total_students as (
    select count(*) total_no_of_students from seat
)
select 
    case when id%2=1 and id=(select total_no_of_students from total_students) then id
    when id%2=1 then id+1
    else id-1
    end id
    , student
from seat
order by id