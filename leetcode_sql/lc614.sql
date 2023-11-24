WITH following_cnt AS
(
	SELECT  follower name
	FROM follow
	GROUP BY  1
	HAVING COUNT(*) >= 1
)
SELECT  followee follower
       ,COUNT(*) num
FROM follow
WHERE followee IN ( 
  select name from following_cnt
 )
GROUP BY  1
HAVING COUNT(*) >= 1
order by 1