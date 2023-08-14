with c as (
    select product_id,
        min(year) first_year
    from sales
    group by product_id
)

select c.product_id,
    c.first_year,
    s.quantity,
    s.price
from c
    inner join sales s
        on s.product_id=c.product_id
           and c.first_year=s.year
;