select player_Id, min(event_date) first_login from activity
group by 1
where exists
        (
                select player_Id from activity
                where year
        )
