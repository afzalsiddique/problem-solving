with points as (
    select *,
        case when host_goals>guest_goals then 3
        when host_goals=guest_goals then 1
        else 0
        end host_point,
        case when guest_goals>host_goals then 3
        when guest_goals=host_goals then 1
        else 0
        end guest_point

    from matches
), points2 as (
    select host_team team_id ,sum(host_point) num_points from points
    group by host_team
    union all
    select guest_team team_id ,sum(guest_point) num_points from points
    group by guest_team
)
select * from points2
select t.team_id,t.team_name,coalesce(sum(p.num_points),0) num_points from teams t
    left join points2 p on p.team_id=t.team_id
group by 1,2
order by 3 desc,1
