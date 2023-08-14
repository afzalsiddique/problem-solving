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

-- two ctes
with f as (  -- first login
	select player_id,
		min(event_date) first
	from activity
	group by player_id
) , c as ( -- logged in next day after first login
	select f.player_id
	from f
		inner join activity a
			on f.player_id=a.player_id
	where datediff(a.event_date,f.first)=1
)

select round(
		(select count(*) from c)/
		(select count(distinct player_id))
	,2)	fraction
from activity