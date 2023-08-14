-- datediff
select activity_date day, count(distinct user_id) active_users
from activity
where datediff('2019-07-27',activity_date) between 0 and 29
group by activity_date
-- date_sub
select activity_date day,
       count(distinct user_id) active_users
from activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
group by activity_date