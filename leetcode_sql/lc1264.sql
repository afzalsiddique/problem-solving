with friends as (
    select case
        when user1_id=1 then user2_id
        when user2_id=1 then user1_id
        else null
        end user_id
    from friendship
), likesOf1 as(
        select page_id from likes
        where user_id=1
)
select distinct page_id recommended_page from likes
    join friends using(user_id)
where page_id not in (select page_id from likesOf1
    )
