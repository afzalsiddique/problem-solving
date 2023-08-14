select distinct num ConsecutiveNums
from logs
where (id+1,num) in (select * from logs)
    and (id+2,num) in (select * from logs)
;
-- 3 self joins
select distinct a.num ConsecutiveNums
from logs a
	inner join logs b
		on a.id+1=b.id
			and a.num=b.num
	inner join logs c
		on b.id+1=c.id
			and b.num=c.num