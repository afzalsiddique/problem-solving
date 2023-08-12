with
t as
(
select count(distinct user_id) total
    from users
)
# select * from t;
select contest_id,
    round(count(*)/(select total from t)*100,2) percentage
from register
group by contest_id
order by 2 desc,1
;