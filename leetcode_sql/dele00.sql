

-- cte
with sRnk as (
    select e.salary,
        row_number() over(order by salary desc) as rn
    from employee e
)

select salary SecondHighestSalary
from sRnk
where sRnk.rn<3
order by sRnk.rn desc
limit 1;

--subquery
select p.product_id,
    round(sum(p.price*u.units)/sum(u.units),2) average_price
from prices p
    inner join unitssold u
        on p.product_id=u.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id;

