with maxx as (
  select count(*) cnt 
  from friends
  group by activity
  order by count(*) desc
  limit 1
), minn as (
  select count(*) cnt 
  from friends
  group by activity
  order by count(*)
  limit 1
), cnt_not_allowed as (
  select * from maxx
  union
  select * from minn
)
select activity
from friends
group by 1
having count(*) not in (select cnt from cnt_not_allowed)