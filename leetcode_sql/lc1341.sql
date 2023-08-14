(
select u.name results
from users u
    inner join movierating r
        on u.user_id=r.user_id
group by u.user_id, u.name
order by count(*) desc, u.name
limit 1
)

union all

(
select m.title results
from movies m
    inner join movierating r
        on m.movie_id=r.movie_id
where date_format(created_at,'%Y-%m')='2020-02'
group by m.movie_id,m.title
order by avg(r.rating) desc, m.title
limit 1
)
