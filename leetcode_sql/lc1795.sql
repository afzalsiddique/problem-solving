with newtable as (
    select product_id,
        case 
            when store1 is null then null
            else 'store1'
        end store,
        store1 as price
    from products
    union 
    select product_id,
        case 
            when store2 is null then null
            else 'store2'
        end store,
        store2 as price
    from products
    union 
    select product_id,
        case 
            when store3 is null then null
            else 'store3'
        end store,
        store3 as price
    from products
)
select * from newtable
where store is not null