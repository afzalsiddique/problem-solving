with rn_table as (
  select *
    , row_number() over(order by id) rn1
  from stadium
)
, people100 as (
  select *
    , row_number() over(order by id) rn2
  from rn_table
  where people>=100
)
, grp_table as (
  select *
    , rn1-rn2 grp_id
  from people100
)
, grp_valid as (
  select distinct grp_id
  from grp_table
  group by grp_id
  having count(*)>=3
)
-- select * from grp_valid
select id
  , visit_date
  , people
from grp_table
where grp_id in (
  select grp_id from grp_valid
)
order by visit_date