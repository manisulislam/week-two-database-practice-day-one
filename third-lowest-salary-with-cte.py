with third_lowest_salary as (

		select distinct salary
		from employees
		order by salary asc
		limit 1
		offset 2

)

select *
from employees
where salary=(
	select salary
	from third_lowest_salary
);


