WITH 
required_dates as (
  select '2013-10-01' request_at
  union 
  select '2013-10-02' request_at
  union 
  select '2013-10-03' request_at
)
,
 not_banned AS
(
	SELECT  id
	       ,client_id
	       ,driver_id
	       ,city_id
	       ,status
	       ,request_at
	FROM trips t
	JOIN users c
	ON t.client_id = c.users_id
	JOIN users d
	ON t.driver_id = d.users_id
	WHERE c.banned = 'No'
	AND d.banned = 'No' 
)
, cte as (
  select request_at
    , sum(
      case when status='completed' then 0
      else 1
      end
    ) cancelled
    , count(*) total
  from not_banned
  group by 1
)
select rd.request_at day
  , coalesce(round(cancelled/total,2) ) 'cancellation rate'
from required_dates rd
join cte
on rd.request_at=cte.request_at