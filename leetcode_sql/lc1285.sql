with my_rank as (
    select log_id, rank() over (order by log_id) num from logs
)
select min(l.log_id) start_id,max(l.log_id) end_id from logs l
    join my_rank using(log_id)
group by l.log_id-num

