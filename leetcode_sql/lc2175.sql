with t1 as (
  select t.team_id
    , t.name
    , points
    , cast(row_number() over(order by points desc,name) as signed) prev_rk
    , points+points_change cur_points
    , cast(row_number() over(order by points+points_change  desc,name) as signed) cur_rk
  from teampoints t
  left join pointschange p
  on t.team_id=p.team_id
  order by cur_rk,name
)
-- select * from t1
select t1.team_id
  , t1.name
  , cast(prev_rk-cur_rk as signed)  rank_diff
from t1