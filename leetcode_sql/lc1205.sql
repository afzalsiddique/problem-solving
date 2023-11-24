select 
  t.id,
  left(t.trans_date,7) month
  , country
  ,
  --  sum(
    case when state='approved' then 1
    else 0
    end
  -- ) 
  approved_count
  ,
  --  sum(
    case when c.trans_date is not null then 1
    else 0
    end
  -- )
   chargeback_count
from transactions t
left join chargebacks c
on t.id=c.trans_id
group by 1,2