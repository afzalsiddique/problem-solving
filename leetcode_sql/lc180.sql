select distinct num ConsecutiveNums
from logs
where (id+1,num) in (select * from logs)
    and (id+2,num) in (select * from logs)
;