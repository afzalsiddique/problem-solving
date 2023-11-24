with dis_logins as (
  select distinct * from logins -- remove duplicates
), add_row as (
  select *
    , row_number() over(partition by id order by login_date) rn
  from dis_logins
), cte as (
  select *
    , lead(login_date,4,'9999-12-31') over(partition by id order by login_date) lead_login
    , lead(rn,4,'9999999') over(partition by id order by login_date) lead_rn
  from add_row
)
select distinct cte.id
  , accounts.name
from accounts
join cte
on cte.id=accounts.id
where datediff(lead_login,login_date)=4
order by id