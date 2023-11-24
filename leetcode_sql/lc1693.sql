select date_id,make_name,count(distinct lead_id) unique_leads,count(distinct partner_id) unique_partners
from dailysales
group by 1,2