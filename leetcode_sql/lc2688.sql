with cte as (
  select *
    , row_number() over() rn
  from users
)
-- select * from cte
select distinct u1.user_id
  -- , u2.created_at
  -- , u1.created_at
  -- , datediff(u2.created_at,u1.created_at) diff
from cte u1
join cte u2
on u1.user_id=u2.user_id
  and u2.created_at>=u1.created_at -- or use abs in where clause
  and u1.rn!=u2.rn
where datediff(u2.created_at,u1.created_at)<=7