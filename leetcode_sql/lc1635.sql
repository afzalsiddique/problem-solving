with RECURSIVE month_series AS (
  SELECT 1 AS month
  UNION ALL
  SELECT month + 1
  FROM month_series
  WHERE month < 12
)
, a (join_month,cnt) as (
  select left(join_date,7) join_month -- yyyy-mm
  , count(*) cnt
  from drivers
  group by 1
  union
  select '1000-01',0 -- ensures every month is selected
)
, b as (
  select join_month
  , sum(cnt) over(order by join_month rows between unbounded preceding and current row) cum_sum
  from a
)
, t_active_drivers as (
  select month 
    , max(cum_sum) active_drivers
  from 
    month_series ms
  join b
  on ms.month>=cast(right(b.join_month,2)as signed)
  where left(b.join_month,4)<=2020 -- "<=" ensures every month is selected
  group by 1
  order by 1
)
, t_accepted_rides as (
  select month
    , count(*) accepted_rides
  from 
    acceptedrides ar
  join 
    rides r
  on r.ride_id=ar.ride_id
  join
    month_series ms
  on month(requested_at)=ms.month
  where year(requested_at)=2020
  group by 1
)
select ad.month
  , coalesce(ad.active_drivers, 0) active_drivers
  , coalesce(ar.accepted_rides,0) accepted_rides
from t_active_drivers ad
left join t_accepted_rides ar
on ad.month=ar.month
order by 1