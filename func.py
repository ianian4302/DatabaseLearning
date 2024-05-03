import sqlite3
database_name = 'MyDatabase.db'
data_root = 'data/'

def check_table_exist(table_name):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 查詢資料表是否存在
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    result = cursor.fetchone()

    # 關閉連線
    conn.close()

    return result is not None

def get_data_info(name):
    #尋找txt檔案中的資料
    with open(data_root + name + '_data.txt', 'r') as file:
        data = file.read().splitlines()
    return data

def insert_data(table_name, datastructure, data ):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 插入資料
    print(f"INSERT INTO {table_name} ({datastructure}) VALUES ({data});")
    cursor.execute(f"INSERT INTO {table_name} ({datastructure}) VALUES ({data});")

    # 關閉連線
    conn.commit()
    conn.close()

def create_table(table_name, columns):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 建立資料表
    cursor.execute(f"CREATE TABLE {table_name} ({columns});")

    # 關閉連線
    conn.commit()
    conn.close()
    
def print_table(table_name):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 查詢指定資料表的欄位名稱
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns_info = cursor.fetchall()

    # 提取欄位名稱並計算每個欄位的最大寬度
    column_names = [col[1] for col in columns_info]
    column_widths = [len(column_name) for column_name in column_names]

    # 查詢資料
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

    # 計算每個欄位的最大寬度
    for row in data:
        for i, value in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(value)))

    # 輸出表格標題
    for i, column_name in enumerate(column_names):
        print(column_name.upper().ljust(column_widths[i]), end='  ')
    print()
    print('-' * (sum(column_widths) + len(column_names) * 2 - 1))  # 分隔線

    # 輸出資料
    for row in data:
        for i, value in enumerate(row):
            print(str(value).ljust(column_widths[i]), end='  ')
        print()

def print_data(data, columns_info):
    column_names = [col[1] for col in columns_info]
    column_widths = [len(column_name) for column_name in column_names]
      # 計算每個欄位的最大寬度
    for row in data:
        for i, value in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(value)))

    # 輸出表格標題
    for i, column_name in enumerate(column_names):
        print(column_name.upper().ljust(column_widths[i]), end='  ')
    print()
    print('-' * (sum(column_widths) + len(column_names) * 2 - 1))  # 分隔線

    # 輸出資料
    for row in data:
        for i, value in enumerate(row):
            print(str(value).ljust(column_widths[i]), end='  ')
        print()

def get_qualifications_player(min_level):
    #SELECT * FROM PLAYER WHERE LEVEL > 10;
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM PLAYER WHERE LEVEL > {min_level};")
    data = cursor.fetchall()
    conn.close()
    return data

def get_qualifications_task(min_level):
    #SELECT * FROM TASK WHERE MIN_LEVEL_NEED > 10;
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TASK WHERE MIN_LEVEL_NEED > {min_level};")
    data = cursor.fetchall()
    conn.close()
    return data

def get_table_title(table_name):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 查詢指定資料表的欄位名稱
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns_info = cursor.fetchall()
    return columns_info

def delet_task(task_id):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # 刪除資料
    cursor.execute(f"DELETE FROM TASK WHERE TASK_ID = {task_id};")

    # 關閉連線
    conn.commit()
    conn.close()
