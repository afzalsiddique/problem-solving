with exp as (
    select project_id, max(experience_years) years from project
        join employee using(employee_id)
    group by 1
)
select p.project_id,p.employee_id from project p
    join exp ex on p.project_id=ex.project_id
    join employee e on p.employee_id=e.employee_id
where e.experience_years=ex.years