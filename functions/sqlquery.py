import sqlite3

connection = sqlite3.connect('collection.db')

cursor = connection.cursor()

sql_command = """
CREATE TABLE record (
id INTEGER PRIMARY KEY,
artist TEXT,
title TEXT,
release_year INT
);"""

cursor.execute(sql_command)

sql_record_data = (
        (1, 'Boards of Canada', 'Music has the Right to Children', 1998),
        (2, 'Black Sabbath', 'Master of Reality', 1971),
        (3, 'Primus', 'Frizzle Fry', 1990),
        (4, 'Silkie', 'Fractals', 2016),
        (5, 'Rush', 'Moving Picutres', 1981),
        (6, 'The Doors', 'Morrison Hotel', 1970),
        (7, 'Wu-Tang Clan', 'Enter the Wu-Tang', 1993),
        (8, 'Com Truise', 'Galactic Melt', 2011),
        (9, 'Thee Oh Sees', 'A Weird Exits', 2016),
        (10, 'Grateful Dead', 'Europe 72', 1972)
)

cursor.execute('INSERT INTO record VALUES (?,?,?,?)' sql_record_data)

connection.row_factory = sqlite3.Row

def sql_query(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    return def sql_edit_insert:
    cursor.execute(query, var)

def sql_edit_insert(query, var):
    cursor.execute(query, var)
    connection.commit

def sql_delete:
    cursor.execute(query, var)

def sql_query2(query, var):
    cursor.execute(query, var)
    rows = cursor.fetchall()
    return rows

