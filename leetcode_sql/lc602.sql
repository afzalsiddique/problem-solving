WITH r AS ( -- received
    SELECT accepter_id AS id, COUNT(*) AS num
    FROM requestAccepted
    GROUP BY accepter_id
), s AS ( -- sent
    SELECT requester_id AS id, COUNT(*) AS num
    FROM requestAccepted
    GROUP BY requester_id
)
(
    SELECT r.id, COALESCE(r.num, 0) + COALESCE(s.num, 0) AS num
    FROM r
    LEFT JOIN s ON r.id = s.id
)
UNION
(
    SELECT s.id, COALESCE(r.num, 0) + COALESCE(s.num, 0) AS num
    FROM r
    RIGHT JOIN s ON r.id = s.id
)
ORDER BY num DESC
LIMIT 1;