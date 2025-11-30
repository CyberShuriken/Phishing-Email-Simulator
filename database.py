import sqlite3
from datetime import datetime

DB_NAME = "phishing.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Table: Targets (People we send emails to)
    c.execute('''CREATE TABLE IF NOT EXISTS targets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    name TEXT
                )''')

    # Table: Campaigns (The phishing event)
    c.execute('''CREATE TABLE IF NOT EXISTS campaigns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')

    # Table: Sent Emails (Links specific targets to campaigns)
    c.execute('''CREATE TABLE IF NOT EXISTS sent_emails (
                    id TEXT PRIMARY KEY, -- This is the unique tracking ID
                    target_id INTEGER,
                    campaign_id INTEGER,
                    status TEXT DEFAULT 'sent', -- sent, clicked
                    clicked_at TIMESTAMP,
                    FOREIGN KEY(target_id) REFERENCES targets(id),
                    FOREIGN KEY(campaign_id) REFERENCES campaigns(id)
                )''')
    
    conn.commit()
    conn.close()
    print(f"Database {DB_NAME} initialized.")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    init_db()
