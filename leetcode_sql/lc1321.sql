WITH cte AS
(
	SELECT  visited_on
	       ,SUM(amount) amount
	FROM customer
	GROUP BY  1
) 
, cte2 AS
(
	SELECT 
        visited_on
        , sum(amount) over(order by visited_on rows BETWEEN 6 preceding AND current row) amount
	       ,round( AVG(amount) over(order by visited_on rows BETWEEN 6 preceding AND current row) ,2 ) average_amount
	       ,row_number() over(order by visited_on) rn
	FROM cte
)
-- select * from cte2
select visited_on
  , amount
  , average_amount
from cte2
WHERE rn >= 7