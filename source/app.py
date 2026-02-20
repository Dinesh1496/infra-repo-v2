from flask import Flask, jsonify
import datetime,socket

app = Flask(__name__)

@app.route('/api/vl/info')
def info():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
    })

@app.route('/api/vl/healthz')
def healthz():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
    
