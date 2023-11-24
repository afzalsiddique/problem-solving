WITH all_player_id AS
(
	SELECT  distinct player_id
	FROM matches
) 
, base_data AS
(
	SELECT  M1.*
	       ,ROW_NUMBER() OVER (PARTITION BY M1.player_id ORDER BY M1.match_day) AS match_seq_num
	FROM Matches M1
)
 , grps AS
(
	SELECT  BD.*
	       ,BD.match_seq_num - ROW_NUMBER() OVER (PARTITION BY BD.player_id ORDER BY BD.match_day) AS grp
	FROM base_data BD
	WHERE BD.result = 'Win' 
)
-- SELECT * FROM grps 
 , all_streaks AS
(
	SELECT  player_id
	       ,COUNT(*) streak
	FROM grps
	GROUP BY  player_id
	         ,grp
)
SELECT  m.player_id
       ,coalesce(MAX(streak),0) longest_streak
FROM matches m
LEFT JOIN all_streaks a
ON m.player_id = a.player_id
GROUP BY  1