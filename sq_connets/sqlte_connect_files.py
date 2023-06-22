import sqlite3

conn = sqlite3.connect('finance_bot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        tg_id INTEGER,
        budget INTEGER,
        expense INTEGER,
        last_purchase TEXT,
        registration_date TEXT,
        last_update_date TEXT,
        is_registered INTEGER DEFAULT 0
    )
''')
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rashodi (
        id INTEGER PRIMARY KEY,
        tg_id INTEGER,
        cars INTEGER,
        food INTEGER,
        cloth TEXT,
        cofe TEXT,
        ucheba TEXT,
        other TEXT
    )
''')
conn.commit()
