-- https://leetcode.com/problems/strong-friendship/solutions/1400657/most-simple-solution/comments/1089690
with T as (
    select user1_id 'user', user2_id 'fid' from Friendship 
    union
    select user2_id 'user', user1_id 'fid' from Friendship 
)
select F.user1_id, F.user2_id , count(*) as 'common_friend' 
from Friendship F, T T1, T T2
where F.user1_id = T1.user 
and F.user2_id = T2.user    
and T1.fid = T2.fid  
group by F.user1_id, F.user2_id
having count(*) >=3