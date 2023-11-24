with perc as (
        select count(*) imm from delivery
                where order_date=customer_pref_delivery_date
), total_count as (
        select count(*) total_count from delivery
)
select round(imm/(select total_count from total_count)*100,2) immediate_percentage from perc