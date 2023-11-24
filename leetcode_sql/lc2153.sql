WITH cte AS
(
	SELECT  b.bus_id
	       ,b.arrival_time
	       ,COUNT(*) cnt
	       ,b.capacity
	FROM buses b
	JOIN passengers p
	ON p.arrival_time <= b.arrival_time
	GROUP BY  1
	ORDER BY 1
)
SELECT  *
       ,cn
    

WITH TEMP AS
(
	SELECT  bus_id
	       ,b.arrival_time
	       ,capacity
	       ,COUNT(passenger_id) AS num
	FROM Buses b
	LEFT JOIN Passengers p
	ON p.arrival_time <= b.arrival_time
	WHERE bus_id is not NULL
	GROUP BY  bus_id
	ORDER BY arrival_time
)
-- SELECT  bus_id
--        ,passengers_cnt
-- FROM
-- (
	SELECT  bus_id
	       ,capacity
	       ,num
	       ,@passengers_cnt:= LEAST(capacity,num-@accum) AS passengers_cnt
	       ,@accum:= @accum+@passengers_cnt
	FROM TEMP,
	(
		SELECT  @accum:= 0
		       ,@passengers_cnt:= 0
	) INIT
-- ) temp
ORDER BY bus_id