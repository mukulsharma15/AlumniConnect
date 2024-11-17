Sure, let's break down the concept of 2NF (Second Normal Form) and how it is violated in the `Professional_History` table with specific examples.

### Basics of 2NF
- **First Normal Form (1NF)**: A table is in 1NF if it contains only atomic (indivisible) values and each column contains values of a single type.
- **Second Normal Form (2NF)**: A table is in 2NF if it is in 1NF and all non-key attributes are fully functionally dependent on the primary key. This means there should be no partial dependency of any column on the primary key.

### Structure of `Professional_History`
The `Professional_History` table has a composite primary key consisting of `JobID` and `AlumniID`. The non-key attributes are `CompanyName`, `JobTitle`, `StartDate`, `EndDate`, and `Skills`.

### Example of 2NF Violation
Consider the following records in the `Professional_History` table:

```sql
INSERT INTO Professional_History (JobID, AlumniID, CompanyName, JobTitle, StartDate, EndDate, Skills)
VALUES 
(5, 4, 'InnoTech', 'Data Analyst', '2013-07-01', '2016-11-30', 'SQL, Python, R'),
(6, 4, 'InnoTech', 'Data Analyst', '2017-01-01', '2020-05-31', 'SQL, Python, R');
```

In this example:
- `JobID` 5 and 6 both belong to `AlumniID` 4.
- `CompanyName` and `JobTitle` are repeated for the same `AlumniID`.

### Explanation of 2NF Violation
- **Partial Dependency**: The non-key attributes `CompanyName` and `JobTitle` are dependent on `AlumniID` alone, not on the entire composite key (`JobID`, `AlumniID`). This means that knowing the `AlumniID` alone is enough to determine the `CompanyName` and `JobTitle`, which violates 2NF.

### Expected Output
When you run the `Check2NF_ProfessionalHistory` procedure, it should detect this partial dependency and raise an error. Here is the expected output:

```sql
CALL Check2NF_ProfessionalHistory();
```

Expected output:

```
ERROR 1644 (45000): The Professional_History table is not in 2NF. Please check for partial dependencies.
```

### Full Example
Here is the full SQL script to insert the data and run the procedure:

```sql
-- Use the AlumniConnect database
USE AlumniConnect;

-- Insert data into Alumni_Info for reference
INSERT INTO Alumni_Info (AlumniID, FirstName, MiddleName, LastName, Email, GradYear, DateOfBirth, CurrentCity)
VALUES 
(4, 'Alice', 'B.', 'Brown', 'alice.brown@example.com', 2013, '1991-04-12', 'San Francisco'),
(5, 'Bob', 'C.', 'Davis', 'bob.davis@example.com', 2014, '1992-08-19', 'Seattle');

-- Insert data into Professional_History that violates 2NF
INSERT INTO Professional_History (JobID, AlumniID, CompanyName, JobTitle, StartDate, EndDate, Skills)
VALUES 
(5, 4, 'InnoTech', 'Data Analyst', '2013-07-01', '2016-11-30', 'SQL, Python, R'),
(6, 4, 'InnoTech', 'Data Analyst', '2017-01-01', '2020-05-31', 'SQL, Python, R'), -- Repeated CompanyName and JobTitle
(7, 5, 'CreativeWorks', 'Graphic Designer', '2014-09-01', '2018-12-15', 'Photoshop, Illustrator, InDesign'),
(8, 5, 'CreativeWorks', 'Graphic Designer', '2019-01-01', '2022-06-30', 'Photoshop, Illustrator, InDesign'); -- Repeated CompanyName and JobTitle

-- Run the procedure to check for 2NF violations
CALL Check2NF_ProfessionalHistory();
```

When you run this script, the `Check2NF_ProfessionalHistory` procedure will detect the partial dependencies and raise an error indicating that the `Professional_History` table is not in 2NF.