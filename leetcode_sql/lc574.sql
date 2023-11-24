WITH t_vote_count AS
(
	SELECT  candidateid
	       ,COUNT(*) vote_count
	FROM vote
	GROUP BY  1
)
select name
from candidate c
join t_vote_count v
on c.id=v.candidateid
where vote_count=(
  select max(vote_count) from t_vote_count
)
