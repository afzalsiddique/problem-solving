select distinct p1.user_Id
  -- , p1.purchase_date
  -- , p2.purchase_date
  -- , datediff(p1.purchase_date,p2.purchase_date) mdiff
from purchases p1
join purchases p2
on p1.user_Id=p2.user_Id
  and p1.purchase_id!=p2.purchase_id   
  and p1.purchase_date<=p2.purchase_date
  and datediff(p2.purchase_date,p1.purchase_date)<=7
order by p1.user_Id