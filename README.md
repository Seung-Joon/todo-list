# todo-list
react-native, django project




## DB Settings
### Set DB charset
```
show variables like '%character%';

set character_set_client = utf8;
set character_set_connection = utf8;
set character_set_database = utf8;
set character_set_filesystem = utf8;
set character_set_results = utf8;
set character_set_server = utf8;
set character_set_system = utf8;


show variables like '%collation%';

set collation_connection = utf8;
set collation_database = utf8;
set collation_server = utf8;
```

### Set DB Local Time (Asia/Seoul)
```
select now(); 

show variables like '%time_zone%'; 

set system_time_zone = 'Asia/Seoul';
```

### DB Schema 
<img src="/DB Schema.png" title="DB Schema"></img>


### DB Definition Query
```
CREATE TABLE `User` (
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `email` varchar(50) NOT NULL UNIQUE,
    `password` varchar(50) NOT NULL,
    `created_date` DATETIME NOT NULL UNIQUE,
    PRIMARY KEY (`user_id`)
);

CREATE TABLE `Todo` (
    `todo_id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `title` varchar(255) NOT NULL UNIQUE,
    `description` varchar(255) NOT NULL UNIQUE,
    `complete` BOOLEAN NOT NULL UNIQUE,
    PRIMARY KEY (`todo_id`)
);

ALTER TABLE `Todo` ADD CONSTRAINT `Todo_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`user_id`);
```
