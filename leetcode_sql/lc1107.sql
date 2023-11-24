-- with t_first_login as 
select login_date, count(*) user_count
from
(
  select user_id,min(activity_date) login_date
  from traffic
  where activity='login'
  group by 1
  having datediff('2019-06-30',min(activity_date))<=90
) t
group by 1

