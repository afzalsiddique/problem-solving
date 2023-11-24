with greatest as (
  select u.name results
  from movierating mr
  join users u
  on u.user_id=mr.user_id
  group by u.user_id
  order by count(*) desc,1
  limit 1
), highest as (
  select m.title results
  from movierating mr
  join movies m
  on mr.movie_id=m.movie_id
  where month(created_at)=2 and year(created_at)=2020
  group by 1
  order by avg(rating) desc,1
  limit 1
)
select * from greatest
union all
select * from highest