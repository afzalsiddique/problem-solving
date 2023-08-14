SELECT s.user_id,
       ROUND(AVG(IF(c.action='confirmed',1,0)),2) as confirmation_rate
FROM Signups s
         LEFT JOIN Confirmations c
                   on c.user_id=s.user_id
GROUP BY s.user_id

-- sol case statement
select s.user_id,
	round(avg(
	    case
			when c.action='confirmed' then 1
			else 0
	        -- wrong. but don't know why
--             when c.action='timeout' then 0
--             else 1
		end
	),2)
	confirmation_rate

from Signups s
	left join confirmations c
		on s.user_id=c.user_id
group by s.user_id
;