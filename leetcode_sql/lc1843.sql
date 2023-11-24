with t0 as (
  select account_id,year(day) year, month(day) month,sum(amount) income
  from transactions
  where type='Creditor'
  group by 1,2,3
  -- order by 1,2
)
-- select * from t0
, t1 as (
  select *
    , case when income>(select max_income from accounts where account_id=t0.account_id)
      then 1
    else 0
    end 'bound'
  from t0
)
-- select * from t1
, t2 as(
  select *
    , row_number() over(partition by account_id order by month) rn
  from t1
  where bound=1
)
-- select * from t2
, t3 as (
  select *
    , year*12+month-rn grp
  from t2
)
-- select * from t3
select distinct account_id
from t3
group by 1,grp
having sum(bound)>=2



