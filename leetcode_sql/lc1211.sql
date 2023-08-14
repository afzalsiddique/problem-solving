select query_name,
   round(avg(rating / position), 2) quality,
   round(
       avg(
           CASE
               when rating < 3 then 1
               else 0
           end
       ) * 100
   , 2)       poor_query_percentage
from queries
group by query_name
