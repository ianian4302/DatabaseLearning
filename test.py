import sqlite3
import func

#init table
#check table exist
if(not func.check_table_exist('NPC')):
    func.create_table('NPC', 'NPC_ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, ADDRESS CHAR(50), SALARY INT')
if(not func.check_table_exist('PLAYER')):
    func.create_table('PLAYER', 'PLAYER_ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, SEX TEXT, LEVEL INT, MONEY INT')
if(not func.check_table_exist('TASK')):
    func.create_table('TASK', 'TASK_ID INT PRIMARY KEY NOT NULL, MIN_LEVEL_NEED INT NOT NULL, DESCRIBE TEXT, AWARD INT')

#init data
#get info from txt
# data = func.get_data_info('NPC')
# for row in data:
#     func.insert_data('NPC', 'NPC_ID, NAME, ADDRESS, SALARY', row)
# data = func.get_data_info('PLAYER')
# for row in data:   
#     func.insert_data('PLAYER', 'PLAYER_ID, NAME,SEX,LEVEL,MONEY', row)
# data = func.get_data_info('TASK')
# for row in data:   
#     func.insert_data('TASK', 'TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD', row)

#check data
func.print_table('TASK')
# func.print_table('PLAYER')
# func.print_table('NPC')

#query data

# #找出符合等級要求的玩家
# data = func.get_qualifications_player(20)
# data_title = func.get_table_title('PLAYER')
# func.print_data(data, data_title)

#找出符合等級要求的任務
data = func.get_qualifications_task(15)
data_title = func.get_table_title('TASK')
func.print_data(data, data_title)

#delete all task from task table
# for i in range(1, 17):
#     func.delet_task(i)

#delete task from task table
#func.delet_task(16)
# func.print_table('TASK')



