WITH install AS
( -- install date of each player 
	SELECT  player_id
	       ,MIN(event_date) install_dt
	FROM activity
	GROUP BY  1
)
-- SELECT * FROM install 
 , no_of_installs AS
(
	SELECT  install_dt
	       ,COUNT(*) installs
	FROM install
	GROUP BY  1
)
-- SELECT * FROM no_of_installs 
 , day1 AS
( -- count of players who logged IN the second day 
	SELECT  i.install_dt
	       ,COUNT(i.player_id) cnt
	FROM install i
	JOIN activity a
	ON a.player_id = i.player_id AND a.event_date = date_add(i.install_dt, interval 1 day)
	GROUP BY  1
)
-- SELECT * FROM day1
SELECT  n.install_dt
       ,installs
       ,round( coalesce(cnt/installs,0) ,2) Day1_retention
FROM no_of_installs n
LEFT JOIN day1 d
ON d.install_dt = n.install_dt