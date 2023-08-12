-- sol 1
SELECT p.product_id,
       ROUND(SUM(u.units*p.price)/SUM(u.units),2) as average_price
FROM Prices p
         INNER JOIN UnitsSold u
              ON p.product_id=u.product_id
                     AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY product_id;
-- sol 2 cte
with
a as
(
    select u.product_id,u.units,p.price
    from unitssold u
        inner join prices p
            on p.product_id=u.product_id
    where u.purchase_date>=p.start_date
        and u.purchase_date<=p.end_date
)
select product_id,
    round(sum(units*price)/sum(units),2) average_price
from a
group by product_id;