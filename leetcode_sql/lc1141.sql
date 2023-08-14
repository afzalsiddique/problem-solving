select activity_date day,
       count(distinct user_id) active_users
from activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
group by activity_date

select activity_date day,
    count(distinct user_id) active_users
from activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
group by activity_date