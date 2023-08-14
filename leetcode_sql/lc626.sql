SELECT
	CASE
		WHEN id % 2 <> 0 AND id = (SELECT COUNT(*) FROM seat) THEN id
		WHEN id % 2 = 0 THEN id - 1
		ELSE
			id + 1
	END as id,
	student
FROM seat
ORDER BY id
;