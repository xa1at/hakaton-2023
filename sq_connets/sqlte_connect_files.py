import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS fn_stats
             (id INTEGER PRIMARY KEY,
              chat_id INTEGER,
              byudjet TEXT,
              posled_rs TEXT,
              tek_schet TEXT,
              time_zp TEXT,
               TEXT)''')
conn.commit()
