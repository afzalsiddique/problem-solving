WITH t AS (
  SELECT
    user_id,
    gender,
    rank() over( PARTITION by gender ORDER BY user_id) rk
  FROM
    genders
)
SELECT user_id, gender FROM t
ORDER BY rk, 2