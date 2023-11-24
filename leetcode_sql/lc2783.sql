WITH t1 AS -- total booking cnt for each flight
(
	SELECT  flight_id
	       ,COUNT(*) total_booking_cnt
	FROM passengers
	GROUP BY  1
)
select f.flight_id
  -- , capacity
  -- , total_booking_cnt
  , case when total_booking_cnt>capacity then capacity
    else coalesce(total_booking_cnt,0)
    end booked_cnt
  , case when total_booking_cnt>capacity then total_booking_cnt-capacity
    else 0
    end waitlist_cnt
from t1
right join flights f
on f.flight_id=t1.flight_id
order by 1