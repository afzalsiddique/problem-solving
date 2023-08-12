SELECT s.user_id,
       ROUND(AVG(IF(c.action='confirmed',1,0)),2) as confirmation_rate
FROM Signups s
         LEFT JOIN Confirmations c
                   on c.user_id=s.user_id
GROUP BY s.user_id
