with t1 as ( -- voting weight of the voter
  select voter
    , 1/count(*) weight
  from votes
  where candidate is not null
  group by 1
)
-- select * from t1
, t2 as ( -- number of votes for each candidate
  select candidate
    , sum(weight) vote
  from votes v
  join t1
  on v.voter=t1.voter
  group by 1
)
-- select * from t2
select candidate
from t2
where vote=(select max(vote) from t2)
order by 1