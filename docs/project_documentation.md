# SOUTH ASIAN UNIVERSITY (SAU)

## DATABASE MANAGEMENT SYSTEM PROJECT

### ALUMNI CONNECT PROJECT

#### Team Members:
- Mukul Sharma (SAU/CS/MSC/2024/08)
- Manvendra Singh Bika (SAU/CS/MSC/2024/07)
- Bhoomi Priya (SAU/CS/IMTECH/2024/01)
- Binwant Kaur (SAU/CS/MSC/2024/06)
- Sharif Abbasi (SAU/CS/MSC/2024/11)

#### Submitted To:
- Dr. Shachi Sharma

---

## Acknowledgment

We would like to express our sincere gratitude to Dr. Shachi Sharma and Mr. Ravendra Ratan Singh for their invaluable guidance, encouragement, and support throughout the development of our project, DBMS Alumni Connect. Dr. Shachi Sharma’s expert advice and insightful suggestions played a pivotal role in shaping the technical and conceptual foundation of this project. Her extensive knowledge and constructive feedback motivated us to delve deeper and refine our work. We are equally grateful to Mr. Ravendra Ratan Singh for his constant mentorship and practical insights, which helped us navigate challenges effectively. His encouragement and technical expertise greatly enhanced the quality of our work. Finally, we extend our thanks to everyone who supported and inspired us during this journey. This project would not have been possible without their contributions.

From,  
Team Members

---

## Abstract

The DBMS Alumni Connect project is designed to create a robust and efficient platform that facilitates communication and collaboration among alumni and current students of an institution. This system enables seamless data management and ensures secure and scalable access to information through its cloud-based infrastructure.

The backend of the project is built using Django and Django Rest Framework (DRF), integrated with a MySQL database hosted on AWS RDS. Advanced database features like triggers and stored procedures are employed to enhance functionality and automate tasks such as notifications and data validation. The frontend offers a user-friendly interface, enabling alumni and students to interact efficiently.

The project focuses on providing key features such as:
- User authentication and role-based access control.
- A searchable alumni directory.
- Messaging or networking functionalities.
- Data analytics for alumni engagement and contributions.

This project leverages modern development practices and cloud hosting to ensure scalability, reliability, and performance. It is a comprehensive solution for institutions seeking to strengthen alumni relationships while offering current students valuable networking opportunities.

---

## Introduction

The DBMS Alumni Connect project aims to bridge the gap between alumni and current students of an institution, creating a platform for meaningful interaction, networking, and collaboration. Alumni play a vital role in the growth of institutions and their current students by contributing to mentorship, placements, and building strong community ties. However, many institutions face challenges in maintaining an active alumni network due to lack of centralized systems and efficient communication channels.

This project addresses these challenges by leveraging modern web technologies and database management systems to develop a scalable and user-friendly solution. The application integrates a secure backend built using Django and Django Rest Framework (DRF) with a MySQL database hosted on AWS RDS. It supports features like user authentication, role-based access, automated notifications, and data-driven analytics.

The frontend of the platform is designed to provide an intuitive and interactive interface, ensuring a seamless user experience. Advanced database techniques, such as triggers and stored procedures, are used to enhance data integrity and automate complex operations.

The DBMS Alumni Connect project not only focuses on reconnecting alumni but also on fostering professional growth opportunities for students, thereby enhancing the overall value of the institution's network. This introduction outlines the foundation of a solution aimed at promoting collaboration and long-term engagement among all stakeholders.

---

## System Architecture

### Description of Backend (Django + Django Rest Framework)

The backend of the DBMS Alumni Connect project is built using Django, a high-level Python web framework, and Django Rest Framework (DRF), a toolkit for building robust and scalable REST APIs. The backend serves as the core of the application, handling data management, business logic, and API interactions. It is designed to ensure security, maintainability, and scalability while providing seamless communication between the frontend and the database.

#### Features of the Backend
1. **User Authentication and Authorization:**
   - Implements secure user login and registration using Django's authentication system.
   - Supports role-based access control (e.g., Alumni, Admin, Student).

2. **RESTful API:**
   - Built using DRF to enable frontend interaction with the backend through HTTP requests.
   - Follows standard REST principles for clean and intuitive API design.

3. **Database Integration:**
   - Uses MySQL for data storage.
   - Supports advanced features such as triggers and stored procedures for automated tasks and enhanced functionality.

4. **Scalability and Performance:**
   - Designed to handle multiple users and requests efficiently.
   - Optimized queries for better performance.

---

## CRUD Operations

The backend provides full CRUD (Create, Read, Update, Delete) functionality for various modules, including alumni info, alumni phone, and achievements, etc.

1. **Create (post()):**
   - Add new records to the database. For example, adding new alumni info in the database.

2. **Read (get()):**
   - Retrieve data from the database. For example, fetching the list of all alumni.

3. **Update (put()):**
   - Modify existing records in the database. For example, updating the phone number of alumni.

4. **Delete (delete()):**
   - Remove records from the database. For example, deleting a user account.

The backend of DBMS Alumni Connect leverages Django and DRF to efficiently handle CRUD operations, ensuring a well-structured and scalable architecture. These operations form the foundation for functionalities like profile management, academic history, and communication within the system, providing a seamless experience for users.

---

### Description of Database (MySQL + AWS RDS)

The database for the DBMS Alumni Connect project is designed using MySQL and hosted on AWS RDS (Relational Database Service). This combination provides a reliable, scalable, and secure solution for managing data. The database is the backbone of the system, ensuring that all data related to alumni, events, and communications is stored, retrieved, and manipulated efficiently.

---

## Database Design

### Tables and Schema

There are six tables and each holds a very important place. These are:
- Alumni info
- Alumni phone
- Academic History
- Achievement
- Professional History
- Social Media

### Triggers

Automate processes and maintain data integrity.

### Procedures

Encapsulate complex queries to simplify application logic.

### ER Diagram

The provided ER (Entity-Relationship) diagram represents the database design for the DBMS Alumni Connect project. It outlines the entities, their attributes, and the relationships among them, which together form the database schema. Below is a detailed explanation:

---

## Entities and Their Attributes

1. **Alumni_info**
   - This is the central entity of the diagram, representing the main details about alumni.
   - Attributes:
     - alumni_id: Unique identifier for each alumni.
     - Fname, Mname, Lname: First, middle, and last name of the alumni.
     - Email: Alumni's email address.
     - GradYear: Year of graduation.
     - Current City: The current city of residence.

2. **Alumni_phone**
   - Represents contact details for alumni.
   - Attributes:
     - alumni_id: Foreign key linking to the Alumni_info entity.
     - country code: Country code of the phone number.
     - mobile number: Phone number of the alumni.

3. **Achievements**
   - Captures information about the alumni's accomplishments.
   - Attributes:
     - Achievement_ID: Unique identifier for each achievement.
     - Award Title: Title of the achievement or award.
     - Description: Description of the achievement.
     - DateAwarded: Date when the achievement was awarded.
     - alumni_id: Foreign key linking to the Alumni_info entity.

4. **Academic_History**
   - Stores the academic records of the alumni.
   - Attributes:
     - Alumni_id: Foreign key linking to the Alumni_info entity.
     - Degree_Name: Name of the degree obtained.
     - Start Year and End Year: Duration of the academic program.
     - CGPA: Cumulative Grade Point Average.

5. **Professional History**
   - Represents the professional details of alumni.
   - Attributes:
     - Job_id: Unique identifier for each job record.
     - Alumni_id: Foreign key linking to the Alumni_info entity.
     - Company Name: Name of the company.
     - Job Title: Designation or title held.
     - Start Date and End Date: Duration of the job.
     - Skills: Skills utilized or acquired during the job.

6. **Social Media**
   - Tracks alumni's social media profiles.
   - Attributes:
     - accountId: Unique identifier for the social media account.
     - alumni_id: Foreign key linking to the Alumni_info entity.
     - Platform: Social media platform (e.g., LinkedIn, Twitter).
     - username: Username of the alumni on the platform.
     - Profile link: URL of the alumni's profile.

---

## Relationships

1. **Alumni_info ↔ Alumni_phone**
   - Relationship: One-to-Many (1:N)
   - An alumni can have multiple phone numbers.

2. **Alumni_info ↔ Achievements**
   - Relationship: One-to-Many (1:N)
   - An alumni can have multiple achievements.

3. **Alumni_info ↔ Academic_History**
   - Relationship: One-to-Many (1:N)
   - An alumni can hold multiple academic records.

4. **Alumni_info ↔ Professional History**
   - Relationship: One-to-Many (1:N)
   - An alumni can have multiple job records in their professional history.

5. **Alumni_info ↔ Social Media**
   - Relationship: One-to-Many (1:N)
   - An alumni can have profiles on multiple social media platforms.

---

## Triggers

Triggers are database mechanisms designed to automatically execute a specified set of instructions in response to certain events on a table, such as insertions, updates, or deletions. In the **DBMS Alumni Connect Project**, triggers were employed to enhance automation, ensure data integrity, and streamline various database operations.

### 1. Insert Triggers

#### Automatic Timestamp
A trigger was implemented to populate the `CreatedTimestamp` column in the `Alumni_Info` table whenever a new record is inserted. This ensures every record is automatically timestamped, aiding in record tracking and auditing.

```sql
ALTER TABLE Alumni_Info ADD CreatedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

CREATE TRIGGER Alumni_Info_Insert_Timestamp
BEFORE INSERT ON Alumni_Info
FOR EACH ROW
SET NEW.CreatedTimestamp = CURRENT_TIMESTAMP;
```

#### Data Validation
Triggers validate data before insertion, such as checking email and phone number formats. Invalid entries are rejected, ensuring data accuracy.

- **Email Validation:**
  ```sql
  DELIMITER //

  CREATE TRIGGER Alumni_Email_Validate
  BEFORE INSERT ON Alumni_Info
  FOR EACH ROW
  BEGIN
      IF NEW.email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email format';
      END IF;
  END //

  DELIMITER ;
  ```

- **Phone Number Validation:**
  ```sql
  DELIMITER //

  CREATE TRIGGER Alumni_Phone_Validate
  BEFORE INSERT ON Alumni_Phone
  FOR EACH ROW
  BEGIN
      IF NEW.mobile_number NOT REGEXP '^[0-9]{10}$' THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid phone number format';
      END IF;
  END //

  DELIMITER ;
  ```

### 2. Audit_Log Triggers

#### Log Changes (Update and Delete)
An `Audit_Log` table records changes made to `Alumni_Info`. Triggers log the `Action_Type`, affected `Record_ID`, and values before and after the change, along with timestamps and user information. This provides a detailed change history for accountability.

- **Update Trigger:**
  ```sql
  CREATE TRIGGER Alumni_Info_Update_Log
  AFTER UPDATE ON Alumni_Info
  FOR EACH ROW
  BEGIN
      INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, New_Value, Changed_By)
      VALUES ('UPDATE', 'Alumni_Info', OLD.alumni_id, OLD.email, NEW.email, USER());
  END;
  ```

- **Delete Trigger:**
  ```sql
  CREATE TRIGGER Alumni_Info_Delete_Log
  BEFORE DELETE ON Alumni_Info
  FOR EACH ROW
  BEGIN
      INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, Changed_By)
      VALUES ('DELETE', 'Alumni_Info', OLD.alumni_id, OLD.email, USER());
  END;
  ```

### 3. Profile Completeness Check
A `ProfileCompletenessPercentage` column is dynamically updated using triggers. This percentage indicates how complete a profile is, based on the presence of key attributes.

- **Insert Trigger:**
  ```sql
  CREATE TRIGGER before_insert_profile_completeness
  BEFORE INSERT ON Alumni_Info
  FOR EACH ROW
  BEGIN
      SET NEW.ProfileCompletenessPercentage = (
          (CASE WHEN NEW.first_name IS NOT NULL THEN 1 ELSE 0 END +
          CASE WHEN NEW.email IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / 6
      );
  END;
  ```

- **Update Trigger:**
  ```sql
  CREATE TRIGGER before_update_profile_completeness
  BEFORE UPDATE ON Alumni_Info
  FOR EACH ROW
  BEGIN
      SET NEW.ProfileCompletenessPercentage = (
          (CASE WHEN NEW.last_name IS NOT NULL THEN 1 ELSE 0 END +
          CASE WHEN NEW.grad_year IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / 6
      );
  END;
  ```

---

## Conclusion

The **DBMS Alumni Connect Project** successfully demonstrates the integration of modern database features and web technologies to create a robust platform for fostering alumni engagement and student networking. The use of **Django** for the backend, combined with **MySQL** on **AWS RDS**, ensures scalability, reliability, and performance. Advanced database techniques, such as triggers and stored procedures, enhance functionality by automating tasks, enforcing data integrity, and providing detailed audit trails.

By offering features like user authentication, a searchable alumni directory, and profile completeness tracking, the project provides significant value to institutions seeking to strengthen their alumni networks. This solution bridges gaps in communication and collaboration, paving the way for meaningful interactions between alumni and students.

Overall, the project highlights the importance of leveraging technology to achieve institutional goals and enrich the professional growth of its community. It stands as a testament to the team's technical expertise, collaborative efforts, and commitment to excellence.
```