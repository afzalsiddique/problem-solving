WITH cte AS
(
	SELECT  person_id
	       ,person_name
	       ,weight
	       ,turn
	       ,SUM(weight) over(order by turn) cum_weight
	FROM queue
)
select person_name from cte
WHERE cum_weight <= 1000 
ORDER BY cum_weight desc
limit 1