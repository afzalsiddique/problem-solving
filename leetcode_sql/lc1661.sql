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

