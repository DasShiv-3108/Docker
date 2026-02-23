from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
import time

app = Flask(__name__)

DB_CONFIG = {
    'host':     os.environ.get('DB_HOST', 'mysql'),
    'port':     int(os.environ.get('DB_PORT', 3306)),
    'user':     os.environ.get('DB_USER', 'appuser'),
    'password': os.environ.get('DB_PASSWORD', 'apppassword'),
    'database': os.environ.get('DB_NAME', 'userprofiles')
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db(retries=10, delay=5):
    for attempt in range(retries):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id             INT AUTO_INCREMENT PRIMARY KEY,
                    full_name      VARCHAR(150) NOT NULL,
                    dob            DATE         NOT NULL,
                    place_of_birth VARCHAR(200) NOT NULL,
                    age            INT          NOT NULL,
                    created_at     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
            print(f"[DB] Connected & table ready (attempt {attempt+1})")
            return
        except Error as e:
            print(f"[DB] Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    raise RuntimeError("MySQL connect failed after retries.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit():
    data           = request.get_json(force=True)
    full_name      = data.get('full_name', '').strip()
    dob            = data.get('dob', '').strip()
    place_of_birth = data.get('place_of_birth', '').strip()
    age            = data.get('age', '')
    if not all([full_name, dob, place_of_birth, age]):
        return jsonify({'success': False, 'message': 'Saare fields zaroori hain!'}), 400
    try:
        conn   = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (full_name, dob, place_of_birth, age) VALUES (%s, %s, %s, %s)",
            (full_name, dob, place_of_birth, int(age))
        )
        conn.commit()
        uid = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'success': True, 'message': f'Profile save ho gaya! ID #{uid}', 'id': uid})
    except Error as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users ORDER BY created_at DESC LIMIT 20")
        rows   = cursor.fetchall()
        cursor.close()
        conn.close()
        for r in rows:
            r['dob']        = str(r['dob'])
            r['created_at'] = str(r['created_at'])
        return jsonify(rows)
    except Error:
        return jsonify([])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
