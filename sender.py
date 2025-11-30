import uuid
import os
import sqlite3
from database import get_db_connection, init_db

# Configuration
BASE_URL = "http://localhost:5000"
OUTPUT_DIR = "sent_emails"

def create_campaign(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO campaigns (name) VALUES (?)", (name,))
    campaign_id = cur.lastrowid
    conn.commit()
    conn.close()
    return campaign_id

def add_target(name, email):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Check if exists
    cur.execute("SELECT id FROM targets WHERE email = ?", (email,))
    row = cur.fetchone()
    
    if row:
        return row[0]
    
    cur.execute("INSERT INTO targets (name, email) VALUES (?, ?)", (name, email))
    target_id = cur.lastrowid
    conn.commit()
    conn.close()
    return target_id

def generate_email(target_name, target_email, campaign_id, template_file):
    unique_id = str(uuid.uuid4())
    tracking_link = f"{BASE_URL}/track/{unique_id}"
    
    # Record in DB
    conn = get_db_connection()
    conn.execute("INSERT INTO sent_emails (id, target_id, campaign_id) VALUES (?, ?, ?)",
                 (unique_id, add_target(target_name, target_email), campaign_id))
    conn.commit()
    conn.close()
    
    # Read template
    with open(template_file, 'r') as f:
        template_content = f.read()
    
    # Replace placeholders
    email_content = template_content.replace('{{ name }}', target_name)
    email_content = template_content.replace('{{ name }}', target_name) # Duplicate just in case
    email_content = email_content.replace('{{ tracking_link }}', tracking_link)
    email_content = email_content.replace('{{ unique_id }}', unique_id)
    
    # Save to file (Simulation)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{OUTPUT_DIR}/{target_name.replace(' ', '_')}_phishing.html"
    
    with open(filename, 'w') as f:
        f.write(email_content)
        
    print(f"[+] Generated email for {target_name}: {filename}")

def main():
    init_db()
    
    print("--- Phishing Campaign Launcher ---")
    campaign_name = "Urgent Invoice Test"
    campaign_id = create_campaign(campaign_name)
    print(f"Created Campaign: {campaign_name}")
    
    targets = [
        ("Alice Smith", "alice@example.com"),
        ("Bob Jones", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com")
    ]
    
    template = "templates/email_urgent.html"
    
    for name, email in targets:
        generate_email(name, email, campaign_id, template)
        
    print(f"\nDone! Check the '{OUTPUT_DIR}' folder for the generated emails.")
    print("Make sure 'python app.py' is running to track the clicks!")

if __name__ == "__main__":
    main()
