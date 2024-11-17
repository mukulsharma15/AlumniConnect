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
    IF NEW.Email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN
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
    IF NEW.MobileNumber NOT REGEXP '^[0-9]{10}$' THEN
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
        'FirstName: ', OLD.FirstName, ', ',
        'MiddleName: ', OLD.MiddleName, ', ',
        'LastName: ', OLD.LastName, ', ',
        'Email: ', OLD.Email, ', ',
        'GradYear: ', OLD.GradYear, ', ',
        'DateOfBirth: ', OLD.DateOfBirth, ', ',
        'CurrentCity: ', OLD.CurrentCity
    );

    SET new_values = CONCAT(
        'FirstName: ', NEW.FirstName, ', ',
        'MiddleName: ', NEW.MiddleName, ', ',
        'LastName: ', NEW.LastName, ', ',
        'Email: ', NEW.Email, ', ',
        'GradYear: ', NEW.GradYear, ', ',
        'DateOfBirth: ', NEW.DateOfBirth, ', ',
        'CurrentCity: ', NEW.CurrentCity
    );

    INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, New_Value, Changed_By)
    VALUES ('UPDATE', 'Alumni_Info', OLD.AlumniID, old_values, new_values, USER());
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
        'FirstName: ', OLD.FirstName, ', ',
        'MiddleName: ', OLD.MiddleName, ', ',
        'LastName: ', OLD.LastName, ', ',
        'Email: ', OLD.Email, ', ',
        'GradYear: ', OLD.GradYear, ', ',
        'DateOfBirth: ', OLD.DateOfBirth, ', ',
        'CurrentCity: ', OLD.CurrentCity
    );

    INSERT INTO Audit_Log (Action_Type, Table_Name, Record_ID, Old_Value, Changed_By)
    VALUES ('DELETE', 'Alumni_Info', OLD.AlumniID, old_values, USER());
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
            (CASE WHEN NEW.FirstName IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.LastName IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.Email IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.GradYear IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.DateOfBirth IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.CurrentCity IS NOT NULL THEN 1 ELSE 0 END)
        ) * 100.0 / 6
    );
END //

-- Create a trigger to update the ProfileCompletenessPercentage column before update
CREATE TRIGGER before_update_profile_completeness
BEFORE UPDATE ON Alumni_Info
FOR EACH ROW
BEGIN
    SET NEW.ProfileCompletenessPercentage = (
        (
            (CASE WHEN NEW.FirstName IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.LastName IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.Email IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.GradYear IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.DateOfBirth IS NOT NULL THEN 1 ELSE 0 END) +
            (CASE WHEN NEW.CurrentCity IS NOT NULL THEN 1 ELSE 0 END)
        ) * 100.0 / 6
    );
END //

DELIMITER ;
```