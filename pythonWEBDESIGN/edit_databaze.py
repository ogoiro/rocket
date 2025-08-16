import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('sqlite.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES user(id)
)
''')

cursor.execute('SELECT id FROM user WHERE username = ?', ('ROCKET',))
user = cursor.fetchone()

if not user:
    cursor.execute(
        'INSERT INTO user (username, password_hash) VALUES (?, ?)',
        ('ROCKET', generate_password_hash('qwerty123'))
    )
    connection.commit()
    user_id = cursor.lastrowid
else:
    user_id = user[0]

cursor.execute('UPDATE post SET author_id = ? WHERE author_id IS NULL', (user_id,))

connection.commit()
connection.close()