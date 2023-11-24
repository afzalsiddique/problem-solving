WITH t AS
(
	SELECT  city_id
	       ,MAX( degree ) degree
	FROM weather
	GROUP BY  1
)
SELECT  w.city_id
       ,MIN( w.day ) day
       ,w.degree
FROM weather w
JOIN t
ON w.city_id = t.city_id
WHERE (w.city_id, w.degree) IN ( SELECT * FROM t)
GROUP BY  1 ,3
order by 1