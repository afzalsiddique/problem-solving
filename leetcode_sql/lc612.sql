select 
  -- p1.x,p1.y,p2.x,p2.y,
   min(round( sqrt(
    (p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y)
    ) 
    ,2))
    shortest
from point2d p1
join point2d p2
on p1.x!=p2.x or p1.y!=p2.y
