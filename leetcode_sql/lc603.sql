with consecutive as (
    select c1.seat_id s1,c2.seat_id s2 from cinema c1
        join cinema c2
        where c1.free=1
            and c2.seat_id=c1.seat_id+1
            and c2.free=1
)
select s1 seat_id from consecutive
union select s2 from consecutive
order by 1