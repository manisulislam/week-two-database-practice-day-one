select *
from employees
where salary=(

		select distinct salary
		from employees
		order by salary asc
		limit 1
		offset 2

);

