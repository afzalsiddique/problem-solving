select min(abs(p1.x-p2.x)) shortest from Point p1
    join Point p2 on p1.x!=p2.x
