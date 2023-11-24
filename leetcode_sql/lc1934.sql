with cte as 
(
    select user_id
        ,
        sum(
            case when action='confirmed' then 1
            else 0
            end
        ) 
        confirmed
        ,count(*) total
    from confirmations
    group by 1
)
select s.user_id
    ,
    coalesce(
        round(
            cte.confirmed/cte.total
        ,2)
    ,0) 
     confirmation_rate
from signups s
left join cte
on cte.user_id=s.user_id
