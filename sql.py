import sqlite3

connection = sqlite3.connect("student1.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT1")

table_info = """
CREATE TABLE STUDENT1(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT1 VALUES('Rapheal', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES('Donatello', 'Machine Learning', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES('Miachelangelo', 'Deep Learning', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES('Rapheal', 'Neural Nets', 'A', 93)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES('Splinter', 'Artificial Intelligence', 'A', 95)''')

print("The inserted records are")

data = cursor.execute('''SELECT * FROM STUDENT1''')

for row in data:
    print(row)

connection.commit()
connection.close()
