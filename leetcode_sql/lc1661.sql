-- solution 1
select a1.machine_id
     , ROUND(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
from Activity a1
         join Activity a2
              on a1.process_id = a2.process_id
                  and a1.machine_id = a2.machine_id
                  and a1.timestamp < a2.timestamp
group by a1.machine_id;

-- solution 2
with p as(
    select a1.machine_id,
           a2.timestamp-a1.timestamp process_time -- end_time-start_time
    from activity a1 -- r1 for start_time
             inner join activity a2 -- r2 for end time
                        on a1.machine_id=a2.machine_id
                            and a1.process_id=a2.process_id
    where a1.activity_type='start'
      and a2.activity_type='end'
)
select machine_id,round(avg(process_time),3) processing_time
from p
group by machine_id;

-- solution 3
with a as
         (select a1.machine_id, a1.process_id, a1.timestamp start, a2.timestamp end
from activity a1
    inner join activity a2
on a1.machine_id=a2.machine_id
    and a1.process_id=a2.process_id
where a1.activity_type='start'
  and a2.activity_type='end'
    )
select machine_id,
       round(avg(end -start), 3) processing_time
from a
group by machine_id
;

