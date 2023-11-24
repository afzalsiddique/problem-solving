-- self join
select a1.player_id, a1.event_date, sum(a2.games_played) games_played_so_far
    from activity a1
        join activity a2 on a1.player_id=a2.player_id
            and a1.event_date>=a2.event_date
group by 1,2

-- window function
select player_id, event_date,
    sum(games_played) over(partition by player_id order by event_date) games_played_so_far
from activity
