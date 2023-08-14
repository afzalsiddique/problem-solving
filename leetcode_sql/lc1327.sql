select p.product_name, sum(o.unit) unit
from products p
    inner join orders o
        on p.product_id=o.product_id
where date_format(order_date, '%Y-%m')='2020-02'
group by p.product_name
having sum(o.unit)>=100