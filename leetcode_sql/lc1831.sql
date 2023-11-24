with max_trans as (
    select date(day) day,max(amount) max_amount from transactions
    group by 1
)
select t.transaction_id from transactions t
    join max_trans mt on date(mt.day)=t.day
        and mt.max_amount=t.amount
order by 1