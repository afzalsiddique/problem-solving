select distinct l1.num ConsecutiveNums
    -- ,l1.*
    -- ,l2.*
    -- ,l3.*
from logs l1 
join logs l2
on l1.id+1=l2.id
    and l1.num=l2.num
join logs l3
on l2.id+1=l3.id
    and l2.num=l3.num