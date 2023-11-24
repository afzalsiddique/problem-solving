with glob_avg as (
    select avg(duration) as glob_avg from calls
), country_duration as(
    select co.name,duration from person p1
        join calls c on c.caller_id=p1.id
        join country co on co.country_code=left(p1.phone_number,3)
    union all
    select co.name,duration from person p2
        join calls c on c.callee_id=p2.id
        join country co on co.country_code=left(p2.phone_number,3)
)
select name country from country_duration
group by country
having avg(duration)>(select glob_avg from glob_avg)