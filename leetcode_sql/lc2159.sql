with t1 as (
  select first_col
    , row_number() over(order by first_col) rn
  from data
)
, t2 as (
  select second_col
    , row_number() over(order by second_col desc) rn
  from data
)
select first_col
  , second_col
from t1
join t2
on t1.rn=t2.rn
