with no_transaction_users as (
  select distinct user_id id
  from users
  where user_id not in (
    select distinct paid_by id
    from transactions
    union
    select distinct paid_to id
    from transactions
  )
)
, -- transaction amount positive or negative
cte as ( 
  select paid_by as id,
    amount*(-1) amount
  from transactions
  union all
  select paid_to as id,
    amount
  from transactions
  union all
  select distinct user_id id
    , 0 amount
  from users
  where user_id  in (
    select id from no_transaction_users
  )
), cte2 as (
  select id
  , sum(amount) amount
  from cte
  group by 1
)

select u.user_id
  , u.user_name
  -- , u.credit
  -- , cte2.amount
  , u.credit+cte2.amount credit
  , case when u.credit+cte2.amount <0 then "Yes"
  else "No"
  end credit_limit_breached
from users u
join cte2
on u.user_id=cte2.id
