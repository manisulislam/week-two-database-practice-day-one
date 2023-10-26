
with third_max_salary as (
		select distinct salary
		from employees
		order by salary desc
		limit 1
		offset 2
)

select *
from employees
where salary= (
	select salary
	from third_max_salary
);





