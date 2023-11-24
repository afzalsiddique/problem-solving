WITH cte1 AS -- create ranking for each seller_id order by order_date
(
	SELECT  o.seller_id
	       ,i.item_id
	       ,i.item_brand
	       ,o.order_date
	       ,rank() over(partition by seller_id ORDER BY order_date) rk
	FROM orders o
	JOIN items i
	ON i.item_id = o.item_id
)
select u.user_id seller_id -- include all the users from the users table using left join
  , case when u.favorite_brand=item_brand then 'yes'
  else 'no'
  end 2nd_item_fav_brand 
from users u
left join cte1
on u.user_id=cte1.seller_id 
  and rk=2