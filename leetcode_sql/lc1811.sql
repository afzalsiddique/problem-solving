with t0 as (
  select gold_medal id, contest_id
  from contests
  union
  select silver_medal id, contest_id
  from contests
  union
  select bronze_medal id, contest_id
  from contests
), t1 as (
  select  id, contest_id
    , row_number() over(partition by id order by contest_id) rn
  from t0
), t2 as (
  select id from t1 -- consecutive
  group by id,contest_id-rn
  having count(*)>=3
  union
  select gold_medal id
  from contests -- gold
  group by gold_medal
  having count(*)>=3
)
select u.name, u.mail
from t2
join users u
on u.user_id=t2.id