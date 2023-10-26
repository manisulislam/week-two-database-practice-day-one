select *
from employees
where salary=(
		select distinct salary
		from employees
		order by salary desc
		limit 1
		offset 2

);



