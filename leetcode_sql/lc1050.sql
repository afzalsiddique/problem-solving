select actor_id, director_id from actordirector
group by 1,2
having count(*)>=3