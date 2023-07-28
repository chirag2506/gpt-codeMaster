import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS users(
    username varchar(100) PRIMARY KEY,
    email varchar(100),
    password varchar(100)
)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS queries(
    username varchar,
    query varchar,
    response varchar
)
''')

cur.execute('''INSERT OR IGNORE INTO users
    VALUES ('test', 'test@test.com', 'test')
''')
conn.commit()

cur.execute('''INSERT OR IGNORE INTO users
    VALUES ('test2', 'test2@test.com', 'test2')
''')
conn.commit()

cur.execute('''INSERT OR IGNORE INTO queries
    VALUES ('test', 'write a python hello world code', 'print("hello world")')
''')
conn.commit()


conn.close()