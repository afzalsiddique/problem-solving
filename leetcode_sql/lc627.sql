-- 1
update Salary set sex=char(ascii('f')+ascii('m')-ascii(sex));

-- 2
update salary set sex=if(sex='m','f','m');