with t1 as (
  select question_id
    , sum(
    case when action='show' then 1
    else 0
    end
    )
    'show_col'
    ,sum(
    case when action='answer' then 1
    else 0
    end
    ) 
    'answer_col'
  from surveylog
  group by 1
)
  select question_id survey_log
    -- , answer_col
    -- ,show_col
    -- ,answer_col/show_col
  from t1
  order by answer_col/show_col desc, question_id
  limit 1