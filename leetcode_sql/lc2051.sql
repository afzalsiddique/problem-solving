with cte as (
  select 
    m.member_id
    , m.name
    , 
    -- coalesce(
      count(p.charged_amount)/count(v.visit_id)
      -- , 0
    -- ) 
    conv
  from members m
  left join visits v
    on m.member_id=v.member_id
  left join purchases p
    on v.visit_id=p.visit_id
  group by 1,2
)
select member_id
  , name
  , case when conv>=0.8 then 'Diamond'
  when conv>=0.5 then 'Gold'
  when conv>=0 then 'Silver'
  else 'Bronze'
  end category
from cte