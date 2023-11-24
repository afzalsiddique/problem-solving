with cte as (
  select requester_id as id from RequestAccepted
  union all
  select accepter_id as id from RequestAccepted
), t_friend_cnt as (
  select id
    , count(*) num
  from cte
  group by 1
)
select id
  , num
from t_friend_cnt
where num=(select max(num) from t_friend_cnt)