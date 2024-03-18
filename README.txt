COMP3005 - A3
Shiven Sharma - 101272855

Instructions:

download the script.py file and execute it from the directory using your terminal or an IDE.
User input is held through CLI, which asks for an operation and any extra information if needed


Database initialization Scripts*

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE NOT NULL
);            

initial test data -- 

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

Youtube demo link: 
https://youtu.be/N8eCnR7sv7w
