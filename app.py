from flask import Flask, render_template, redirect, url_for, request
from database import get_db_connection, init_db
from datetime import datetime

app = Flask(__name__)

# Ensure DB exists on startup
init_db()

@app.route('/')
def dashboard():
    conn = get_db_connection()
    
    # Get stats
    total_sent = conn.execute('SELECT COUNT(*) FROM sent_emails').fetchone()[0]
    total_clicked = conn.execute("SELECT COUNT(*) FROM sent_emails WHERE status = 'clicked'").fetchone()[0]
    
    # Get recent clicks
    recent_clicks = conn.execute('''
        SELECT t.name, t.email, c.name as campaign, s.clicked_at
        FROM sent_emails s
        JOIN targets t ON s.target_id = t.id
        JOIN campaigns c ON s.campaign_id = c.id
        WHERE s.status = 'clicked'
        ORDER BY s.clicked_at DESC
        LIMIT 10
    ''').fetchall()
    
    conn.close()
    return render_template('dashboard.html', sent=total_sent, clicked=total_clicked, recent=recent_clicks)

@app.route('/track/<unique_id>')
def track_click(unique_id):
    conn = get_db_connection()
    
    # Check if ID exists
    email_record = conn.execute('SELECT * FROM sent_emails WHERE id = ?', (unique_id,)).fetchone()
    
    if email_record:
        # Record the click if not already clicked (or update timestamp)
        conn.execute('''
            UPDATE sent_emails 
            SET status = 'clicked', clicked_at = ? 
            WHERE id = ?
        ''', (datetime.now(), unique_id))
        conn.commit()
        print(f"[!] CLICK DETECTED: {unique_id}")
    else:
        print(f"[?] Unknown ID clicked: {unique_id}")
        
    conn.close()
    
    # Redirect to the "Education" page (The "Gotcha!" page)
    return redirect(url_for('education'))

@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == '__main__':
    print("Starting Phishing Simulator Server...")
    print("Dashboard: http://localhost:5000")
    app.run(debug=True, port=5000)
