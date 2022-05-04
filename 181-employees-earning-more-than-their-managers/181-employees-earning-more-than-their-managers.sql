/* Write your PL/SQL query statement below */
select e1.name as "Employee" from Employee e1 where salary> (select salary from Employee e2 where e2.id=e1.managerId)