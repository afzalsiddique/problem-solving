
with c as (
select delivery_id,
    min(order_date)=min(customer_pref_delivery_date) Immediate
    from delivery
    group by customer_id
)
select round(sum(Immediate)/count(*)*100,2) immediate_percentage
from c

--
with f as (
	select customer_id
	from delivery
	group by customer_id
	having min(order_date)=min(customer_pref_delivery_date)
)


select round(
	(select count(*) from f)
	/(select count(distinct customer_id) from Delivery)
	*100,2)

	immediate_percentage
