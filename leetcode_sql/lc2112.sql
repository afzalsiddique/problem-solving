with t0 as (
  select departure_airport a1
    , arrival_airport a2
    , flights_count
  from flights
  union
  select arrival_airport a1
    , departure_airport a2
    , flights_count
  from flights
), t1 as (
  select a1 airport_id
    , sum(flights_count)
    , rank() over(order by sum(flights_count) desc) rk
  from t0
  group by 1
)
select airport_id from t1
where rk=1