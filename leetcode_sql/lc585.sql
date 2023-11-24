with same_2015 as (
  select distinct i1.tiv_2015 from insurance i1
  where i1.tiv_2015 in (
    select i2.tiv_2015 from insurance i2
    where i1.pid!=i2.pid
      and i1.tiv_2015=i2.tiv_2015
  )
), diff_city as (
  select i1.lat, i1.lon from insurance i1
  where (i1.lat,i1.lon) not in (
    select i2.lat,i2.lon from insurance i2
    where i1.lat!=i2.lat
      and i1.lon!=i2.lon
      and i1.pid!=i2.pid
  )
)

with same_2015 as (
  select tiv_2015 from insurance
  group by 1
  having count(*)>1
),
diff_city as (
  select lat,lon from insurance
  group by 1,2
  having count(*)=1
)
select round(sum(tiv_2016),2) tiv_2016
from insurance
where tiv_2015 in (select * from same_2015)
  and (lat,lon) in (select * from diff_city)