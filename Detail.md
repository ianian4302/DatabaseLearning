#	Database System Final projet

##	410985004 陳文彥

##	簡介
由三個tale組成：NPC / PLAYER / TASK
由NPC發布任務，由PLAYER接收任務。
任務有最低等級要求，可透過查詢府何等級的任務或玩家

---
###	Full code in Github
[Code Link There](https://github.com/ianian4302/DatabaseLearning)

<font size = 3>
	
---
##	查詢
```py=
#query data

#找出符合等級要求的玩家
data = func.get_qualifications_player(10)
data_title = func.get_table_title('PLAYER')
func.print_data(data, data_title)

#找出符合等級要求的任務
data = func.get_qualifications_task(10)
data_title = func.get_table_title('TASK')
func.print_data(data, data_title)

#delete task from task table
func.delet_task(11)
func.print_table('TASK')

```

---
##	ER-model
![image](/assests/1.png)

---
##	Relational Database Schema
![image](/assests/2.png)

<div style="page-break-after: always;"></div>
	
---
	
<font size = 2>
	
##	Detail
###	init table
check table exist or not, create table if not exist. 
```py=
#init table
#check table exist
if(not func.check_table_exist('NPC')):
    func.create_table('NPC', 
	'NPC_ID 	INT PRIMARY KEY NOT NULL,
	 NAME   	TEXT            NOT NULL,
	 ADDRESS 	CHAR(50),
	 SALARY 	INT')
if(not func.check_table_exist('PLAYER')):
    func.create_table('PLAYER',
	'PLAYER_ID    INT PRIMARY KEY     NOT NULL,
	 NAME         TEXT                NOT NULL,
	 SEX          TEXT,
	 LEVEL        INT,
	 MONEY        INT')
if(not func.check_table_exist('TASK')):
    func.create_table('TASK',
	'TASK_ID          INT PRIMARY KEY     NOT NULL,
	 MIN_LEVEL_NEED   INT                 NOT NULL,
	 DESCRIBE         TEXT,
	 AWARD            INT')
```

###	init data from file
```py=
#init data
#get info from txt
data = func.get_data_info('NPC')
for row in data:
    func.insert_data('NPC', 'NPC_ID, NAME, ADDRESS, SALARY', row)
data = func.get_data_info('PLAYER')
for row in data:   
    func.insert_data('PLAYER', 'PLAYER_ID, NAME,SEX,LEVEL,MONEY', row)
data = func.get_data_info('TASK')
for row in data:   
    func.insert_data('TASK', 'TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD', row)
```

###	check data
```py=
#check data
func.print_table('TASK')
func.print_table('PLAYER')
func.print_table('NPC')
```

</font>
	
<div style="page-break-after: always;"></div>
	
---
##	Result
###	table of TASK
```shell=
TASK_ID  MIN_LEVEL_NEED  DESCRIBE                                          AWARD  
---------------------------------------------------------------------------------
2        8               Gather materials for crafting                     300
3        15              Defeat boss in dungeon                            800
4        7               Deliver goods to another city                     400
5        12              Escort NPC to safety                              600
6        6               Hunt monsters in the forest                       350
7        18              Explore mysterious ruins                          1000
8        9               Help villagers with their problems                450
9        14              Retrieve stolen artifacts                         700
10       5               Train new recruits                                250
12       17              Investigate paranormal activity                   950
13       13              Rescue hostages from enemy stronghold             650
14       19              Slay mythical creatures                           1100
15       16              Retrieve ancient artifacts from forbidden temple  900
16       20              Confront evil sorcerer in final showdown          1200
1        10              Complete quest A                                  500
```

###	table of NPC
```sh=
NPC_ID  NAME      ADDRESS    SALARY  
------------------------------------
1       Albert    Taiwan     1000
2       Benjamin  USA        2000
3       Charlie   Canada     3000
4       Daniel    Australia  4000
5       Edward    Germany    5000
6       Frank     France     6000
7       George    Japan      7000
8       Henry     China      8000
9       Isaac     India      9000
10      Jacob     Russia     10000
11      Kevin     Italy      11000
12      Liam      Spain      12000
13      Michael   Brazil     13000
14      Nathan    Mexico     14000
15      Oliver    Argentina  15000
16      Patrick   Chile      16000
```

###	table of PLAYER
```sh=
PLAYER_ID  NAME     SEX     LEVEL  MONEY
-----------------------------------------
1          Alice    Female  20     5000
2          Bob      Male    15     4000
3          Charlie  Male    25     7000
4          David    Male    12     3000
5          Emma     Female  28     9000
6          Frank    Male    18     6000
7          Grace    Female  23     8000
8          Henry    Male    17     5500
9          Ivy      Female  30     10000
10         Jack     Male    21     7200
11         Kevin    Male    13     3600
12         Linda    Female  19     6400
13         Mike     Male    22     7800
14         Nancy    Female  11     2500
15         Olivia   Female  27     8800
16         Peter    Male    16     5100
```

###	找出符合等級要求的玩家
```sh=
#找出符合等級要求的玩家
data = func.get_qualifications_player(20)
data_title = func.get_table_title('PLAYER')
func.print_data(data, data_title)
```
###	符合等級要求的玩家列表
```sh=
PLAYER_ID  NAME     SEX     LEVEL  MONEY  
----------------------------------------- 
3          Charlie  Male    25     7000   
5          Emma     Female  28     9000   
7          Grace    Female  23     8000   
9          Ivy      Female  30     10000  
10         Jack     Male    21     7200   
13         Mike     Male    22     7800   
15         Olivia   Female  27     8800  
```

###	找出符合等級要求的任務
```sh=
#找出符合等級要求的任務
data = func.get_qualifications_task(20)
data_title = func.get_table_title('TASK')
func.print_data(data, data_title)
```

###	符合等級要求的任務
```sh=
TASK_ID  MIN_LEVEL_NEED  DESCRIBE                                          AWARD  
---------------------------------------------------------------------------------
7        18              Explore mysterious ruins                          1000
12       17              Investigate paranormal activity                   950
14       19              Slay mythical creatures                           1100
15       16              Retrieve ancient artifacts from forbidden temple  900
16       20              Confront evil sorcerer in final showdown          1200
```

###	delete task from task table, [TASK_ID = 16]
```sh=
#delete task from task table
func.delet_task(16)
func.print_table('TASK')
```

###	result after delete task of [TASK_ID = 16]
```sh=
TASK_ID  MIN_LEVEL_NEED  DESCRIBE                                          AWARD  
---------------------------------------------------------------------------------
1        10              Complete quest A                                  500
2        8               Gather materials for crafting                     300
3        15              Defeat boss in dungeon                            800
4        7               Deliver goods to another city                     400
5        12              Escort NPC to safety                              600
6        6               Hunt monsters in the forest                       350
7        18              Explore mysterious ruins                          1000
8        9               Help villagers with their problems                450
9        14              Retrieve stolen artifacts                         700
10       5               Train new recruits                                250
11       11              Clear out bandit camps                            550
12       17              Investigate paranormal activity                   950
13       13              Rescue hostages from enemy stronghold             650
14       19              Slay mythical creatures                           1100
15       16              Retrieve ancient artifacts from forbidden temple  900
```
</font>