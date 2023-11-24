select gender
  , day
  , sum(score_points) over(partition by gender order by day) total
from scores
order by 1,2