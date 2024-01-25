
create table callers
(
    caller_id   int auto_increment
        primary key,
    caller_name varchar(255) not null
);


create table cities
(
    city_id   int auto_increment
        primary key,
    city_name varchar(255) not null
);


create table calls
(
    call_id              int auto_increment
        primary key,
    caller_id            int          null,
    city_id              int          null,
    phone_number         varchar(20)  null,
    short_description    text         null,
    detailed_description text         null,
    call_address         varchar(255) null,
    call_date            date         null,
    call_time            time         null,
    constraint calls_ibfk_1
        foreign key (caller_id) references callers (caller_id),
    constraint calls_ibfk_2
        foreign key (city_id) references cities (city_id)
);

create index caller_id
    on calls (caller_id);

create index city_id
    on calls (city_id);

create table emergency_reasons
(
    emergency_reason_id int auto_increment
        primary key,
    call_id             int  not null,
    reason_description  text null
);

create table rescuers
(
    rescuer_id   int auto_increment
        primary key,
    rescuer_name varchar(255) not null
);

create table injuries
(
    injury_id   int auto_increment
        primary key,
    call_id     int          null,
    rescuer_id  int          not null,
    description text         null,
    hospital    varchar(255) null,
    diagnosis   text         null,
    constraint injuries_ibfk_1
        foreign key (call_id) references calls (call_id),
    constraint injuries_ibfk_2
        foreign key (rescuer_id) references rescuers (rescuer_id)
);

create index call_id
    on injuries (call_id);

create index rescuer_id
    on injuries (rescuer_id);

create table rescuer_calls
(
    rescuer_call_id int auto_increment
        primary key,
    call_id         int  not null,
    rescuer_id      int  not null,
    dispatch_time   time not null,
    return_time     time null,
    constraint rescuer_calls_ibfk_1
        foreign key (call_id) references calls (call_id),
    constraint rescuer_calls_ibfk_2
        foreign key (rescuer_id) references rescuers (rescuer_id)
);

create index call_id
    on rescuer_calls (call_id);

create index rescuer_id
    on rescuer_calls (rescuer_id);

create table vehicles
(
    vehicle_id   int auto_increment
        primary key,
    vehicle_name varchar(255) not null
);


create table call_vehicles
(
    call_vehicle_id int auto_increment
        primary key,
    call_id         int  not null,
    vehicle_id      int  not null,
    dispatch_time   time not null,
    return_time     time null,
    constraint call_vehicles_ibfk_1
        foreign key (call_id) references calls (call_id),
    constraint call_vehicles_ibfk_2
        foreign key (vehicle_id) references vehicles (vehicle_id)
);

create index call_id
    on call_vehicles (call_id);

create index vehicle_id
    on call_vehicles (vehicle_id);
    
    DELIMITER $$

CREATE TRIGGER PreventDuplicateStreetName
BEFORE INSERT ON street
FOR EACH ROW
BEGIN
    DECLARE count_names INT;
    SELECT COUNT(*) INTO count_names FROM street WHERE street_name = NEW.street_name AND city_id = NEW.city_id;
    IF count_names > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate street name for the same city is not allowed';
    END IF;
END$$

DELIMITER ;
DELIMITER //

CREATE PROCEDURE InsertCity(IN cityName VARCHAR(255) )
BEGIN
    INSERT INTO cities (city_name) VALUES (cityName);
END//

DELIMITER ;  
-- Створення пакета для вставки 10 стрічок у таблицю vehicles
DELIMITER //

CREATE PROCEDURE InsertVehicles()
BEGIN
    DECLARE counter INT DEFAULT 1;
    
    WHILE counter <= 10 DO
        -- Вставка рядка у таблицю vehicles
        INSERT INTO vehicles (vehicle_name) VALUES (CONCAT('Noname', counter));
        
        -- Інкремент лічильника
        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;  
DELIMITER //

CREATE FUNCTION FindMaxCallerId()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE max_id INT;
    SELECT MAX(caller_id) INTO max_id FROM callers;
    RETURN max_id;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE GetMaxCallerId()
BEGIN
    DECLARE max_id INT;
    SET max_id = FindMaxCallerId();
    SELECT max_id;
END //

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE CopyDataToRandomTables()
BEGIN
    DECLARE table1_name VARCHAR(255);
    DECLARE table2_name VARCHAR(255);
    DECLARE done INT DEFAULT FALSE;
    DECLARE cursor_vehicle CURSOR FOR SELECT CONCAT('call_vehicle_', UNIX_TIMESTAMP()) AS table_name;
    DECLARE cursor_rescuer CURSOR FOR SELECT CONCAT('call_rescuer_', UNIX_TIMESTAMP()) AS table_name;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Створення першої таблиці
    OPEN cursor_vehicle;
    FETCH cursor_vehicle INTO table1_name;
    SET @sql1 = CONCAT('CREATE TABLE ', table1_name, ' LIKE call_vehicle');
    PREPARE stmt1 FROM @sql1;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;
    
    -- Створення другої таблиці
    OPEN cursor_rescuer;
    FETCH cursor_rescuer INTO table2_name;
    SET @sql2 = CONCAT('CREATE TABLE ', table2_name, ' LIKE call_rescuer');
    PREPARE stmt2 FROM @sql2;
    EXECUTE stmt2;
    DEALLOCATE PREPARE stmt2;
    
    CLOSE cursor_vehicle;
    CLOSE cursor_rescuer;
    
    -- Копіювання даних
    SET @copy_sql = CONCAT('INSERT INTO ', IF(RAND() < 0.5, table1_name, table2_name), ' SELECT * FROM ', IF(RAND() < 0.5, 'call_vehicle', 'call_rescuer'));
    PREPARE copy_stmt FROM @copy_sql;
    EXECUTE copy_stmt;
    DEALLOCATE PREPARE copy_stmt;
    
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER CheckPhoneNumberEnding
BEFORE INSERT ON calls
FOR EACH ROW
BEGIN
    DECLARE phone_end CHAR(2);
    SET phone_end = RIGHT(NEW.phone_number, 2);
    IF phone_end = '00' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Phone number cannot end with two zeros';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER CheckRescuerName
BEFORE INSERT ON rescuers
FOR EACH ROW
BEGIN
    IF NEW.rescuer_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid rescuer name. Allowed names are: Svitlana, Petro, Olha, Taras';
    END IF;
END$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER PreventEmergencyReasonModification
BEFORE UPDATE ON emergency_reasons
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Modification of data in emergency_reason table is not allowed';
END$$

CREATE TRIGGER PreventEmergencyReasonDeletion
BEFORE DELETE ON emergency_reasons
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Deletion of data from emergency_reason table is not allowed';
END$$

DELIMITER ;







 

