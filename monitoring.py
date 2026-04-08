import time
import random
from flask import Flask, jsonify
import telepot

# Data collection function
def collect_data():
    # Simulates data collection (replace with actual data gathering logic)
    data = {
        'cpu_usage': random.randint(0, 100),
        'memory_usage': random.randint(0, 100),
        'disk_usage': random.randint(0, 100)
    }
    return data

# Anomaly detection function
def detect_anomalies(data):
    anomalies = []
    # Simple anomaly detection based on arbitrary thresholds (replace with actual logic)
    if data['cpu_usage'] > 80:
        anomalies.append("High CPU usage")
    if data['memory_usage'] > 80:
        anomalies.append("High Memory usage")
    if data['disk_usage'] > 80:
        anomalies.append("High Disk usage")
    return anomalies

# Telegram notification function
def send_telegram_alert(message):
    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    bot = telepot.Bot(bot_token)
    bot.sendMessage(chat_id, message)

# Flask web server setup
app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    data = collect_data()
    return jsonify(data)

# Terminal UI function
def run_terminal_ui():
    while True:
        data = collect_data()
        print(f"CPU Usage: {data['cpu_usage']}% | Memory Usage: {data['memory_usage']}% | Disk Usage: {data['disk_usage']}%")
        
        anomalies = detect_anomalies(data)
        if anomalies:
            message = "\n".join(anomalies)
            print("Anomalies detected:", message)
            send_telegram_alert(message)
        
        time.sleep(5)

if __name__ == '__main__':
    # Start terminal UI in a separate thread
    import threading
    ui_thread = threading.Thread(target=run_terminal_ui)
    ui_thread.start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=5000)