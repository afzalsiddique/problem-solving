select name,sum(amount) balance from transactions t
    inner join users u on t.account=u.account
    group by t.account
    having sum(amount)>10000