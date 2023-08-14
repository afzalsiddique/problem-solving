-- find out firstLogin for every player_id with cte
with cte as 
(
    select player_id,
        min(event_date) firstLogin
    from activity
    group by player_id
)
select round(
            count(cte.player_id)
            /(select count(distinct player_id) from activity)
            ,2) 
            fraction
from cte
    inner join activity a
        on cte.player_id=a.player_id
            and dateDiff(a.event_date,cte.firstLogin)=1
            ;