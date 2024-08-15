Create Database NodeTask;

use NodeTask;

Create Table Employee
(
	employee_id int primary key, first_name VARCHAR(100) Not Null, last_name VARCHAR(100) Not Null, email VARCHAR(100) Unique Not Null,
    phone_number Varchar(12), hire_date DATE Not Null, salary DECIMAL(10, 2), manager_id int,
	Foreign key(manager_id) references Employee(employee_id), department_id int,
    foreign key(department_id) references Departments(department_id)
);

INSERT INTO Employee (employee_id, first_name, last_name, email, phone_number, hire_date, salary, manager_id, department_id)
VALUES
  (5, 'John', 'Doe', 'johndoe@example.com', '1234567890', '2023-11-22', 50000.00, 2, 1),
  (6, 'Jane', 'Smith', 'janesmith@example.com', '9876543210', '2022-05-15', 60000.00, 3, 2),
  (7, 'Michael', 'Johnson', 'michaeljohnson@example.com', '1112223333', '2021-08-01', 45000.00, 3, 1),
  (8, 'Emily', 'Brown', 'emilybrown@example.com', '4445556666', '2024-02-10', 55000.00, 4, 3),
  (9, 'David', 'Lee', 'davidlee@example.com', '7778889999', '2023-09-15', 62000.00, 5, 2);

Select * from Employee;

Create Table Departments
(
	department_id int Primary Key, department_name VARCHAR(100) Not Null, location VARCHAR(200)
);

Insert into Departments values(1, "Innovation Labs", "MCity"), (2, "MApps", "Mcity");
Select * from Departments;

Create Table Projects
(
	project_id int PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2), department_id int,
    FOREIGN KEY(department_id) REFERENCES Departments(department_id)
);

Insert into Projects values(1, "Clearner Staff Pro", "2024-08-14", "2024-08-20", 6700000.00, 1);
Insert into Projects values(2, "Fake product using GenAI", "2024-08-20", "2024-11-20", 9899000.00, 1), 
                           (3, "Healthcare diagnosis using AI", "2024-10-22", "2025-12-22", 45612312.00, 1);
Select * from Projects;

Create Table Employee_Projects
(
	employee_id int, project_id int, role VARCHAR(50), hours_worked DECIMAL(5, 2) , Primary Key(employee_id, project_id),
    foreign key(employee_id) references Employee(employee_id), 
    foreign key(project_id) references Projects(project_id)
);

Select e.employee_id from employee e join employee_projects ep on e.employee_id = ep.employee_id join  Projects p  on  ep.project_id = p.project_id where p.end_date > "2024-08-13" and e.employee_id = 1;


Select e.employee_id from Employee e join Employee_Projects ep on e.employee_id = ep.employee_id where role = "Manager";

Insert into Employee_Projects values(1, 1, "Manager", 9.2), (2, 2, "Developer", 10.5), (3, 1, "HR", 8);
Select * from Employee_Projects;

truncate Employee_projects;

Select * from employee;
select employee_id from Employee where employee_id = manager_id;

