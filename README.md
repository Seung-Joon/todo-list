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
<img src="https://i.imgur.com/a7yx6ER.png" title="DB Schema"></img>
