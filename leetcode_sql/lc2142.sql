with cte as (
  SELECT  passenger_id
        ,p.arrival_time
        ,( -- bus that arrives the earliest after the passenger
          select 
            bus_id
          from buses
          where arrival_time>=p.arrival_time
          order by arrival_time
          limit 1
        ) bus_id
  FROM passengers p
)
-- select * from cte

select b.bus_id
  , count(passenger_id) passengers_cnt
from buses b
left join cte 
on b.bus_id=cte.bus_id
group by 1
order by 1

