with c as (
    select account_id,
        case
            when income<20000 then 'Low Salary'
            when income>=20000 and income<=50000 then 'Average Salary'
            else 'High Salary'
        end category
    from accounts
),
t as (
    select 'Low Salary' as cat
    union
    select 'Average Salary' as cat
    union
    select 'High Salary' as cat
)
select t.cat category, count(c.account_id) accounts_count -- count(c.account_id) -> to avoid null values
from t
    left join c
        on t.cat=c.category
group by t.cat