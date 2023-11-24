with wins as (
    select wimbledon player_id, count(*) count 
    from championships
    group by 1
    union all
    select fr_open player_id, count(*) count 
    from championships
    group by 1
    union all
    select us_open player_id, count(*) count 
    from championships
    group by 1
    union all
    select au_open player_id, count(*) count 
    from championships
    group by 1
)
select p.*,sum(wins.count) grand_slams_count  from wins
    join players p using(player_id)
group by 1,2