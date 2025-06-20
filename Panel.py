from flask import Flask, render_template, request
import threading
import time

app = Flask(__name__)
bot_running = False

def run_bot():
    global bot_running
    bot_running = True
    while bot_running:
        print("Bot is running...")
        time.sleep(5)  # Simulasi kerja bot

@app.route('/')
def index():
    return render_template('index.html', bot_running=bot_running)

@app.route('/start', methods=['POST'])
def start_bot():
    if not bot_running:
        threading.Thread(target=run_bot).start()
    return index()

@app.route('/stop', methods=['POST'])
def stop_bot():
    global bot_running
    bot_running = False
    return index()

if __name__ == '__main__':
    app.run(debug=True)
