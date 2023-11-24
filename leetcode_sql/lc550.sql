with t_first_login as (
  select player_id, min(event_date) first_login
  from activity
  group by 1
)
select 
  -- a.player_id
  -- , 
  round(
    sum(
      case when a.event_date=date_add(first_login, interval 1 day) then 1
        else 0
        end 
    )/(select  count(distinct player_id) no_of_total_player from activity)
  ,2)
  fraction
from activity a
join t_first_login f
on a.player_id=f.player_id