WITH t_rn AS
(
	SELECT  *
	       ,row_number() over(partition by username ORDER BY endDate desc,startdate desc) rn
	FROM userActivity
) , second_recent AS
(
	SELECT  username
	       ,activity
	       ,startdate
	       ,enddate
	FROM t_rn
	WHERE rn = 2 
) 
, second_recent_names AS
(
	SELECT  distinct username
	FROM second_recent
) , most_recent AS
(
	SELECT  username
	       ,activity
	       ,startdate
	       ,enddate
	FROM t_rn
	WHERE rn = 1 
)
SELECT  *
FROM second_recent
UNION
SELECT  *
FROM most_recent
where username not in (select * from second_recent_names)