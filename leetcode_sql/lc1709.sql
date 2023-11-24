-- use lead
with t_visit_diff as (
    select user_id, 
        datediff(lead(visit_date,1,'2021-1-1') over(partition by user_id order by visit_date) ,visit_date)
        visit_diff
    from uservisits
)
select user_id, max(visit_diff) biggest_window
from t_visit_diff
group by 1


-- 
with my_rank as (
    select user_id, visit_date,
        rank() over(partition by user_id order by visit_date desc) rk
    from uservisits
), tmp_table as (
    select r1.user_id,
        max(datediff(r2.visit_date,r1.visit_date)) wind
    from my_rank r1
    join my_rank r2
        on r1.user_id=r2.user_id
        and r1.rk=r2.rk+1
    group by 1

    union 

    select r.user_id,
        datediff('2021-1-1',r.visit_date) wind
    from my_rank r
    where r.rk=1
)
select user_id,max(wind) biggest_window from tmp_table
group by 1
order by 1
