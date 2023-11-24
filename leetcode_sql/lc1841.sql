-- do it again. avoid code duplication

--
with tmp as (
  select team_id
    , team_name
    , count(*) matches_played
    , sum(
      case when home_team_goals>away_team_goals then 3
      when home_team_goals=away_team_goals then 1
      else 0
      end 
    ) points
    , sum(home_team_goals) goal_for
    , sum(away_team_goals) goal_against
    , sum(home_team_goals)-sum(away_team_goals) goal_diff
  from teams t
  join matches m1
  on m1.home_team_id=t.team_id
  group by 1,2

  union 


  select team_id
    , team_name
    , count(*) matches_played
    , sum(
      case when home_team_goals<away_team_goals then 3
      when home_team_goals=away_team_goals then 1
      else 0
      end 
    ) points
    , sum(away_team_goals) goal_for
    , sum(home_team_goals) goal_against
    , sum(away_team_goals)-sum(home_team_goals) goal_diff
  from teams t
  join matches m1
  on m1.away_team_id=t.team_id
  group by 1,2
)
select team_name
  , sum(matches_played) matches_played
  , sum(points) points
  , sum(goal_for) goal_for
  , sum(goal_against) goal_against
  , sum(goal_diff) goal_diff
from tmp
group by 1
order by 3 desc, 6 desc, 1