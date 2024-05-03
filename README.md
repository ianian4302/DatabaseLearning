# Database Learning

### Get start
```sh
sqlite3 DatabaseName.db
```

### HELP
```sh
sqlite>.help
```

### Create Database
```sh
sqlite>.open test.db
```

### Format output ans show table
```sh
sqlite>.header on
sqlite>.mode column
sqlite>.timer on
sqlite>SELECT * FROM table_name;
```

### Check table ans get full imformation
```sh
sqlite>.tables
sqlite>.schema [TableName]
```

### Delet table
```sh
sqlite>DROP TABLE [tablename];
```


```sql
CREATE TABLE NPC(
   NPC_ID       INT PRIMARY KEY     NOT NULL,
   NAME         TEXT                NOT NULL,
   ADDRESS      CHAR(50),
   SALARY       INT
);


INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (1, 'Albert', 'Taiwan', 1000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (2, 'Benjamin', 'USA', 2000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (3, 'Charlie', 'Canada', 3000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (4, 'Daniel', 'Australia', 4000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (5, 'Edward', 'Germany', 5000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (6, 'Frank', 'France', 6000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (7, 'George', 'Japan', 7000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (8, 'Henry', 'China', 8000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (9, 'Isaac', 'India', 9000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (10, 'Jacob', 'Russia', 10000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (11, 'Kevin', 'Italy', 11000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (12, 'Liam', 'Spain', 12000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (13, 'Michael', 'Brazil', 13000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (14, 'Nathan', 'Mexico', 14000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (15, 'Oliver', 'Argentina', 15000);
INSERT INTO NPC (NPC_ID, NAME, ADDRESS, SALARY) VALUES (16, 'Patrick', 'Chile', 16000);


CREATE TABLE PlAYER(
   PLAYER_ID    INT PRIMARY KEY     NOT NULL,
   NAME         TEXT                NOT NULL,
   SEX          TEXT,
   LEVEL        INT,
   MONEY        INT
);

INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (1, 'Alice', 'Female', 20, 5000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (2, 'Bob', 'Male', 15, 4000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (3, 'Charlie', 'Male', 25, 7000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (4, 'David', 'Male', 12, 3000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (5, 'Emma', 'Female', 28, 9000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (6, 'Frank', 'Male', 18, 6000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (7, 'Grace', 'Female', 23, 8000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (8, 'Henry', 'Male', 17, 5500);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (9, 'Ivy', 'Female', 30, 10000);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (10, 'Jack', 'Male', 21, 7200);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (11, 'Kevin', 'Male', 13, 3600);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (12, 'Linda', 'Female', 19, 6400);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (13, 'Mike', 'Male', 22, 7800);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (14, 'Nancy', 'Female', 11, 2500);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (15, 'Olivia', 'Female', 27, 8800);
INSERT INTO PLAYER (PLAYER_ID, NAME, SEX, LEVEL, MONEY) VALUES (16, 'Peter', 'Male', 16, 5100);


CREATE TABLE TASK(
   TASK_ID          INT PRIMARY KEY     NOT NULL,
   MIN_LEVEL_NEED   INT                 NOT NULL,
   DESCRIBE         TEXT,
   AWARD            INT
);

INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (1, 10, 'Complete quest A', 500);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (2, 8, 'Gather materials for crafting', 300);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (3, 15, 'Defeat boss in dungeon', 800);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (4, 7, 'Deliver goods to another city', 400);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (5, 12, 'Escort NPC to safety', 600);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (6, 6, 'Hunt monsters in the forest', 350);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (7, 18, 'Explore mysterious ruins', 1000);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (8, 9, 'Help villagers with their problems', 450);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (9, 14, 'Retrieve stolen artifacts', 700);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (10, 5, 'Train new recruits', 250);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (11, 11, 'Clear out bandit camps', 550);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (12, 17, 'Investigate paranormal activity', 950);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (13, 13, 'Rescue hostages from enemy stronghold', 650);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (14, 19, 'Slay mythical creatures', 1100);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (15, 16, 'Retrieve ancient artifacts from forbidden temple', 900);
INSERT INTO TASK (TASK_ID, MIN_LEVEL_NEED, DESCRIBE, AWARD) VALUES (16, 20, 'Confront evil sorcerer in final showdown', 1200);
