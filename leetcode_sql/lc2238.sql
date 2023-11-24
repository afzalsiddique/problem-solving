select r1.driver_id
  -- , r1.ride_id
  -- , r2.ride_id
  , count(distinct r2.ride_id) cnt -- distinct r1.ride_id will not work. coz left join
from rides r1 -- driver
left join rides r2 -- passenger
  on r1.driver_id=r2.passenger_id
group by 1
