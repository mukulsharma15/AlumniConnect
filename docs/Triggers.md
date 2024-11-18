### 1. Insert Triggers

#### Automatic Timestamp
Create a `CreatedTimestamp` column in the `Alumni_Info` table and a trigger to set it on insert.

```sql
ALTER TABLE Alumni_Info ADD CreatedTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

CREATE TRIGGER Alumni_Info_Insert_Timestamp
BEFORE INSERT ON Alumni_Info
FOR EACH ROW
SET NEW.CreatedTimestamp = CURRENT_TIMESTAMP;
```

#### Data Validation
Create a trigger to validate email and phone number formats.

```sql
--Email
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

--Phone Number
DELIMITER //

CREATE TRIGGER Alumni_Phone_Validate
BEFORE INSERT ON Alumni_Phone
FOR EACH ROW
BEGIN
    IF NEW.country_code NOT REGEXP '^[0-9]{1,5}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid country code format';
    END IF;
    IF NEW.mobile_number NOT REGEXP '^[0-9]{10}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid phone number format';
    END IF;
END //

DELIMITER ;
```

### 2. Audit_Log (Update/Delete) Triggers

#### Log Changes
Create an `Audit_Log` table and a trigger to log changes.

```sql
CREATE TABLE Audit_Log (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    Action_Type VARCHAR(10),
    Table_Name VARCHAR(50),
    Record_ID INT,
    Old_Value TEXT,
    New_Value TEXT,
    Changed_By VARCHAR(50),
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


--Update Trigger
DELIMITER //

CREATE TRIGGER Alumni_Info_Update_Log
AFTER UPDATE ON Alumni_Info
FOR EACH ROW
BEGIN
    DECLARE old_values TEXT;
    DECLARE new_values TEXT;

    SET old_values = CONCAT(
        'FirstName: ', OLD.first_name, ', ',
        'MiddleName: ', OLD.middle_name, ', ',
        'LastName: ', OLD.last_name, ', ',
        'Email: ', OLD.email, ', ',
        'GradYear: ', OLD.grad_year, ', ',
        'DateOfBirth: ', OLD.date_of_birth, ', ',
        'CurrentCity: ', OLD.current_city
    );

    SET new_values = CONCAT(
        'FirstName: ', NEW.first_name, ', ',
        'MiddleName: ', NEW.middle_name, ', ',
        'LastName: ', NEW.last_name, ', ',
        'Email: ', NEW.email, ', ',
        'GradYear: ', NEW.grad_year, ', ',
        'DateOfBirth: ', NEW.date_of_birth, ', ',
        'CurrentCity: ', NEW.current_city
    );

    INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, New_Value, Changed_By)
    VALUES ('UPDATE', 'Alumni_Info', OLD.alumni_id, old_values, new_values, USER());
END //

DELIMITER ;

--Delete Trigger
DELIMITER //

CREATE TRIGGER Alumni_Info_Delete_Log
BEFORE DELETE ON Alumni_Info
FOR EACH ROW
BEGIN
    DECLARE old_values TEXT;

    SET old_values = CONCAT(
        'FirstName: ', OLD.first_name, ', ',
        'MiddleName: ', OLD.middle_name, ', ',
        'LastName: ', OLD.last_name, ', ',
        'Email: ', OLD.email, ', ',
        'GradYear: ', OLD.grad_year, ', ',
        'DateOfBirth: ', OLD.date_of_birth, ', ',
        'CurrentCity: ', OLD.current_city
    );

    INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, Changed_By)
    VALUES ('DELETE', 'Alumni_Info', OLD.alumni_id, old_values, USER());
END //

DELIMITER ;
```

### 3. Profile Completeness Check
Add a `ProfileCompletenessPercentage` column and a trigger to update it.

```sql
-- Add the ProfileCompletenessPercentage column
ALTER TABLE Alumni_Info
ADD ProfileCompletenessPercentage DECIMAL(5, 2);

-- Create a trigger to update the ProfileCompletenessPercentage column before insert
DELIMITER //

CREATE TRIGGER before_insert_profile_completeness
BEFORE INSERT ON Alumni_Info
FOR EACH ROW
BEGIN
    SET NEW.ProfileCompletenessPercentage = (
        (
            (CASE WHEN NEW.first_name IS NOT NULL AND NEW.first_name != 'default_first_name' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.last_name IS NOT NULL AND NEW.last_name != 'default_last_name' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.email IS NOT NULL AND NEW.email != 'default_email@example.com' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.grad_year IS NOT NULL AND NEW.grad_year != 0 THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.date_of_birth IS NOT NULL AND NEW.date_of_birth != '1900-01-01' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.current_city IS NOT NULL AND NEW.current_city != 'default_city' THEN 1 ELSE 0 END)
        ) * 100.0 / 6
    );
END //

DELIMITER ;

-- Create a trigger to update the ProfileCompletenessPercentage column before update
DELIMITER //

CREATE TRIGGER before_update_profile_completeness
BEFORE UPDATE ON Alumni_Info
FOR EACH ROW
BEGIN
    SET NEW.ProfileCompletenessPercentage = (
        (
            (CASE WHEN NEW.first_name IS NOT NULL AND NEW.first_name != 'default_first_name' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.last_name IS NOT NULL AND NEW.last_name != 'default_last_name' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.email IS NOT NULL AND NEW.email != 'default_email@example.com' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.grad_year IS NOT NULL AND NEW.grad_year != 0 THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.date_of_birth IS NOT NULL AND NEW.date_of_birth != '1900-01-01' THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.current_city IS NOT NULL AND NEW.current_city != 'default_city' THEN 1 ELSE 0 END)
        ) * 100.0 / 6
    );
END //

DELIMITER ;