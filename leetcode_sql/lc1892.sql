-- 'not exists' is faster than 'not in'
-- works
with friends(user1_id,user2_id) as (
  select user1_id,user2_id
  from friendship
  union all
  select user2_id,user1_id
  from friendship
)
select user1_id user_id
  , page_id 
  , count(user2_id ) friends_likes
from likes l
join friends f
on l.user_id=f.user2_id
where not exists (select * from likes 
  where user_id=user1_id and page_id=l.page_id)
group by 1,2
-- order by 1,3 -- visualization only

-- TLE
with friends(user1_id,user2_id) as (
  select user1_id,user2_id
  from friendship
  union all
  select user2_id,user1_id
  from friendship
)
select user1_id user_id
  , page_id 
  , count(user2_id ) friends_likes
from likes l
join friends f
on l.user_id=f.user2_id
where (user1_id,page_id) not in (select * from likes) -- replace this 'not in' with 'not exists'
group by 1,2
-- order by 1,3 -- visualization only

-- lc solution
-- first, prep a table that contains all users and their friends
with t1 as (
    select user1_id as user_id, user2_id as friend_id from friendship
    union
    select user2_id as user_id, user1_id as friend_id from friendship)
    
-- then, join table
select t1.user_id, l.page_id, count(distinct t1.friend_id) as friends_likes
from t1
join likes as l
on t1.friend_id=l.user_id

-- filter out pages that are already liked by the user
left join likes as l2
on t1.user_id=l2.user_id and l.page_id=l2.page_id
where l2.page_id is null

-- get the final output
group by t1.user_id, l.page_id
