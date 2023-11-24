WITH base_fail AS
(
	SELECT  fail_date
	       ,row_number() over(order by fail_date) rn
	FROM failed
  where fail_date between '2019-01-01' and '2019-12-31'
)
, grp_fail as (
  select fail_date
    , date_sub(fail_date,interval rn day) grp
  from base_fail
)
, base_success AS
(
	SELECT  success_date
	       ,row_number() over(order by success_date) rn
	FROM succeeded
  where success_date between '2019-01-01' and '2019-12-31'
)
, grp_success as (
  select success_date
    , date_sub(success_date,interval rn day) grp
  from base_success
)
, all_dates (period_state, start_date,end_date) as (
  select 'failed', min(fail_date),max(fail_date)
  from grp_fail
  group by grp
  union
  select 'succeeded', min(success_date), max(success_date)
  from grp_success
  group by grp
)
select * from all_dates
order by start_date