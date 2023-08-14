select user_id,
       concat(upper(SUBSTR(name, 1, 1)),
              lower(substr(name, 2, length(name)))
           ) as name
from users
order by user_id;
