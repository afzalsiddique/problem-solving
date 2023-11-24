-- solution 1
with scores as (
  select first_player player_id
    , first_score score
  from matches
  union all
  select second_player player_id
    , second_score score
  from matches
)
-- select * from scores
, score_table as (
  select player_id
    , sum(score) score
  from scores
  group by 1
)
-- select * from score_table
, rank_table as (
  select  p.player_id
    , score
    , group_id
    , rank() over(partition by group_id order by score desc, p.player_id) rk
  from score_table s
  join players p
  on p.player_id=s.player_id
)
select group_id
  , player_id
from rank_table
where rk=1

-- solution 2
with scores as (
  select first_player player_id
    , first_score score
  from matches
  union all
  select second_player player_id
    , second_score score
  from matches
)
-- select * from scores
, score_table as (
  select p.player_id
    , sum(score) score 
    , max(group_id) group_id -- dummy max
    , rank() over(partition by group_id order by sum(score) desc, p.player_id) rk
  from scores s
  join players p
  on p.player_id=s.player_id
  group by 1
)
-- select * from score_table
select group_id
  , player_id
from score_table
where rk=1
