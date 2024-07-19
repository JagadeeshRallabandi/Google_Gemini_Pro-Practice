import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
table_info="""
create table STUDENT(Name Varchar(25),Class Varchar(25),Section Varchar(25),Marks INT);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Jagadeesh','Data Science','A','90')''')
cursor.execute('''Insert Into STUDENT values('Dinesh','AI','B','100')''')
cursor.execute('''Insert Into STUDENT values('Krish','Maths','C','99')''')
cursor.execute('''Insert Into STUDENT values('Ramesh','Machine Learning','A','69')''')
cursor.execute('''Insert Into STUDENT values('Suresh','Science','C','9')''')
cursor.execute('''Insert Into STUDENT values('Deepika','Data Science','A','10')''')
cursor.execute('''Insert Into STUDENT values('Ramu','Data Science','C','69')''')
print("The inserted record are")
data=cursor.execute('''Select* From Student''')

for row in data:
    print(row)
    
connection.commit()
connection.close()