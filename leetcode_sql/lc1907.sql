with sal as(
  select "Low Salary" as category
  union
  select "Average Salary" as category
  union
  select "High Salary" as category
)
, cat as (
  select account_id,income
  , case when income<20000 then "Low Salary"
  when income<=50000 then "Average Salary"
  else "High Salary"
  end category
  from accounts
)
select sal.category, count(account_id) accounts_count
from sal
left join cat
on sal.category=cat.category
group by 1