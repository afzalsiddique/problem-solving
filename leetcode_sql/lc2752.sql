with t_row_no as (
  select customer_id
    , transaction_date
    , row_number() over(partition by customer_id order by transaction_date) rn
  from transactions
), 
t_consecutive as (
  select customer_id
    ,
    count(
      date_sub(transaction_date, interval rn day)
      )
      no_of_consecutive_trans_date -- start_date of consecutive transaction dates
  from t_row_no
  group by 1,date_sub(transaction_date, interval rn day)
)
select  customer_id
from t_consecutive
where no_of_consecutive_trans_date=(
  select max(no_of_consecutive_trans_date) consecutive_days
  from t_consecutive
)
order by 1