with teamsize as (
    select team_id, count(*) as team_size from employee
    group by 1
)
select employee_id, team_size from employee
     join teamsize using(team_id)