select account_id,day,
  sum(
    case when type='Deposit' then amount
    else amount*(-1)
    end 
  ) over(partition by account_id order by day)
  balance
from transactions
