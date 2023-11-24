select user_id, steps_date, rolling_average
from (
  select user_id
    , steps_count
    , steps_date
    , round(
      avg(steps_count) over(partition by user_id order by steps_date rows between 2 preceding and current row) 
      , 2
    )
    rolling_average
    , lag(steps_date,2) over(partition by user_id order by steps_date) two_dates_prev
  from steps
) temp
where datediff(steps_date,two_dates_prev)=2
order by 1,2