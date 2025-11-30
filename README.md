# 🎣 Phishing Email Simulator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-green)

A security awareness tool that simulates phishing attacks to help organizations train employees. It generates realistic phishing emails, tracks user clicks in real-time, and provides educational feedback to victims.

## 🧐 The Problem

Phishing remains the #1 delivery vector for malware and ransomware. Technical controls (firewalls, spam filters) are essential, but the "human firewall" is often the weakest link. Companies need safe, controlled ways to test and train employees without exposing them to real threats.

## 💡 The Solution

This simulator allows security teams to:
1.  **Launch Campaigns**: Create realistic scenarios (e.g., "Urgent Invoice", "Password Reset").
2.  **Track Behavior**: Monitor who clicks the malicious links in real-time.
3.  **Educate**: Immediately redirect users to a safe "teachable moment" page explaining what they missed.

**Note:** This tool includes a **"Simulation Mode"** that generates HTML files instead of sending real emails, allowing for safe local testing without SMTP configuration.

## 🚀 Features

- **Campaign Management**: Organize tests by specific scenarios.
- **Real-Time Tracking**: Unique tracking IDs for every target ensure 100% accurate click attribution.
- **Live Dashboard**: Visual stats on Sent vs. Clicked emails.
- **Teachable Moments**: Custom landing pages that educate rather than punish.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/phishing-simulator.git
    cd phishing-simulator
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### 1. Start the Tracking Server
This runs the dashboard and the tracking listener.
```bash
python app.py
```
*Access the dashboard at `http://localhost:5000`*

### 2. Launch a Phishing Campaign
Open a new terminal to run the campaign generator.
```bash
python sender.py
```
This will generate simulated email files in the `sent_emails/` directory.

### 3. Verify
Open any generated `.html` file in `sent_emails/` and click the link. Watch the dashboard update instantly!

## 🧠 Skills Demonstrated

- **Web Development**: Building a Flask application with routes, templates, and static assets.
- **Database Design**: Using SQL (SQLite) to track relationships between campaigns, targets, and events.
- **Social Engineering**: Understanding the psychology behind successful phishing attacks (urgency, authority).
- **Security Operations**: Implementing the "Test, Track, Train" loop used in professional security programs.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
