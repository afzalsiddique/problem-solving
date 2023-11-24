select name warehouse_name, sum(width*length*height*units) volume from warehouse w
        inner join products p on p.product_id=w.product_id
group by 1