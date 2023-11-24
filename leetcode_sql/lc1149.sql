select distinct viewer_id id
from views
group by viewer_id, view_date
having count(distinct article_id)>1
order by 1