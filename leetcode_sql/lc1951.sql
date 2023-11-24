with t0 as (
  select r1.user_id user1_id
    , r2.user_id user2_id
    , count(*) common_followers
    , rank() over(order by count(*) desc) rk
  from relations r1
  join relations r2
  on r1.user_id<r2.user_id
    and r1.follower_id=r2.follower_id
  group by 1,2
  -- order by 1,2,3
)
-- select * from t0
select user1_id, user2_id
from t0
where rk=1
group by 1,2