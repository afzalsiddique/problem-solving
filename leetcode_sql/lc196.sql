delete p1 from person as p1, person as p2 -- 'as' is optional
    where p1.email=p2.email and p1.id>p2.id;
