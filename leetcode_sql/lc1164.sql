with lastChange as
(
    select product_id, max(change_date) lastDate
    from products
    where change_date<='2019-08-16'
    group by product_id
),
T2 as
(
    select product_id, new_price
    from products
    where (product_id,change_date) in (select * from lastChange)
)
select T1.product_id, ifnull(t2.new_price,10) price 
from (select distinct product_id from products) T1
    left join T2
        on T1.product_id=T2.product_id
;
-- union
with lastChange as (
    select product_id,
           max(change_date) last_date
    from products
    where change_date<='2019-08-16'
    group by product_id
)
select lastChange.product_id,
       p.new_price price
from lastChange
         inner join products p
                    on p.product_id=lastChange.product_id
                        and lastChange.last_date=p.change_date

union

select product_id, 10
from products
group by product_id
having min(change_date)>'2019-08-16'



