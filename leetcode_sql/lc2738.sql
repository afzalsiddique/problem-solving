select 'bull' as word
  , sum(content like '% bull %') count
from files
union
select 'bear' as word
  , sum(content like '% bear %') count
from files


SELECT 'bull' as word
  ,
  SUM(length(content)-length(replace(content,'bull','')))/length('bull') count 
FROM files

union

SELECT 'bear' as word
  ,
  SUM(length(content)-length(replace(content,'bear','')))/length('bear') count 
FROM files