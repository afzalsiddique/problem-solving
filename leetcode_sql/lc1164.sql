with lead_date as (
    select product_id
        , new_price
        , change_date
        , lead(change_date,1,'9999-12-12') over(partition by product_id order by change_date) next_date
    from products
),
new_price as (
    select product_id
        , case when '2019-08-16'>=change_date and '2019-08-16'<next_date then new_price
        else null
        end price
    from lead_date
), cte as (
    select * from new_price
    where price is not null
)
select distinct p.product_id
    , 
    coalesce(
        cte.price,10
    ) price
from products p
left join cte
on p.product_id=cte.product_id