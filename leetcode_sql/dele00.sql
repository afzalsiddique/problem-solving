select p.product_id,
    round(sum(p.price*u.units)/sum(u.units),2) average_price
from prices p
    inner join unitssold u
        on p.product_id=u.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id;
