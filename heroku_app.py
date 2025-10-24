"""
Client-Side Motion Detection System for Heroku Deployment
Each device uses its own camera through WebRTC
"""

from flask import Flask, render_template, jsonify, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with client-side camera access"""
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """
    Optional server-side processing endpoint
    For now, we'll do everything client-side
    """
    try:
        data = request.get_json()
        # In the future, you could add server-side AI processing here
        return jsonify({'success': True, 'message': 'Frame processed'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/health')
def health():
    """Health check endpoint for Heroku"""
    return jsonify({'status': 'healthy', 'message': 'Motion Detection System is running'})

if __name__ == '__main__':
    # Get port from environment variable (Heroku requirement)
    port = int(os.environ.get('PORT', 5000))
    
    print("=" * 60)
    print("🎯 CLIENT-SIDE MOTION DETECTION SYSTEM")
    print("=" * 60)
    print("📱 Each device uses its own camera")
    print("🌐 Heroku deployment ready")
    print("🚀 Starting server...")
    print("=" * 60)
    
    # Run with Heroku-compatible settings
    app.run(debug=False, host='0.0.0.0', port=port)