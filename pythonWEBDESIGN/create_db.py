import sqlite3

connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS post (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES user(id)
    );
''')

connection.commit()
connection.close()

print("База данных успешно создана.")