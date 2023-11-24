with t_avg as (
  select event_type
    , avg(occurences) avg_occ
    from events
    group by 1
), cte as (
  select business_id
    , case when e.occurences>
      (select avg_occ from t_avg where t_avg.event_type=e.event_type) then 1
    else 0
    end occ
  from events e
)
select business_id
from cte
group by 1
having sum(occ)>1
