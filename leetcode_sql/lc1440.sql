
select left_operand,operator,right_operand, case 
        when operator='<' and v1.value<v2.value then 'true'
        when operator='=' and v1.value=v2.value then 'true'
        when operator='>' and v1.value>v2.value then 'true'
        else 'false'
        end value
from expressions
inner join variables v1 on v1.name=left_operand
inner join variables v2 on v2.name=right_operand
    