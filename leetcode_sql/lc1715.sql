with including_chest as (
  select b.*
    , case when b.chest_id is null then 0
    else c.apple_count
    end c_apple_count
    , case when b.chest_id is null then 0
    else c.orange_count
    end c_orange_count
  from boxes b
  join chests c
  on b.chest_id=c.chest_id
  or b.chest_id is null
), unique_chest as (
  select distinct * from including_chest
)
select sum(apple_count)+sum(c_apple_count) apple_count
, sum(orange_count)+sum(c_orange_count) orange_count
from unique_chest