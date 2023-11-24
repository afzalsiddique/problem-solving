select name from customers c
    where c.id not in 
        (select distinct customerId from orders)