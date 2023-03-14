select name as customers from customers
    where id not in (select distinct customerId from orders);
