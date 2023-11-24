with rootnode as (
    select id from tree
    where p_id is null
), innerAndRoot as (
    select distinct p_id as id from tree
        where p_id is not null
    union
    select id from rootnode
) , justInner as (
    select ir.id from innerAndRoot ir
    join tree t using(id)
    where id not in (
        select id from rootnode
    )
), leafnode as (
    select id from tree
    where id not in (
        select id from innerAndRoot
    )
)
select id, 'Leaf' as type from leafnode
union
select id,'Root' as type from rootnode
union
select id,'Inner' as  type from justInner