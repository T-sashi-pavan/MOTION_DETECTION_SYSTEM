"""
Enhanced Client-Side Human Motion Detection System for Heroku Deployment
Matching functionality from motion_detection_CV.py
Each device uses its own camera through WebRTC
"""

from flask import Flask, render_template, jsonify, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with enhanced client-side motion detection"""
    return render_template('index_enhanced.html')

@app.route('/original')
def original():
    """Original basic motion detection (fallback)"""
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """
    Optional server-side processing endpoint
    For now, we'll do everything client-side for privacy
    """
    try:
        data = request.get_json()
        # In the future, you could add server-side AI processing here
        return jsonify({'success': True, 'message': 'Frame processed'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/features')
def api_features():
    """API endpoint showing enhanced features"""
    return jsonify({
        'system': 'Enhanced Human Motion Detection System',
        'features': [
            'Multiple people detection',
            'Skin color analysis for human identification',
            'Human shape filtering (aspect ratio validation)',
            'Background subtraction simulation (MOG2 style)',
            'Morphological operations for noise reduction',
            'Overlap removal with IoU calculation',
            'Real-time frame processing (30 FPS)',
            'Motion intensity analysis',
            'Contour area filtering',
            'Bounding box optimization'
        ],
        'detection_methods': [
            'Motion-based detection with human filtering',
            'Skin color detection in HSV space',
            'Shape analysis (width/height ratios)',
            'Area thresholding for human-sized objects',
            'Multi-frame stabilization'
        ],
        'privacy': 'All processing happens in browser - no data sent to servers',
        'technology': 'Client-side WebRTC + Advanced JavaScript algorithms',
        'compatibility': 'Works on phones, tablets, desktops',
        'source_inspiration': 'motion_detection_CV.py with OpenCV and MediaPipe'
    })

@app.route('/health')
def health():
    """Health check endpoint for Heroku"""
    return jsonify({
        'status': 'healthy', 
        'message': 'Enhanced Human Motion Detection System is running',
        'version': '2.0',
        'capabilities': 'Multiple people detection with advanced algorithms'
    })

if __name__ == '__main__':
    # Get port from environment variable (Heroku requirement)
    port = int(os.environ.get('PORT', 5000))
    
    print("=" * 80)
    print("🎯 ENHANCED HUMAN MOTION DETECTION SYSTEM")
    print("=" * 80)
    print("✅ Multiple people detection")
    print("✅ Skin color analysis") 
    print("✅ Human shape filtering")
    print("✅ Background subtraction simulation")
    print("✅ Advanced contour processing")
    print("✅ Real-time frame analysis")
    print("📱 Each device uses its own camera")
    print("🌐 Heroku deployment ready")
    print("🔒 Privacy-focused (client-side processing)")
    print("🚀 Starting enhanced server...")
    print("=" * 80)
    
    # Run with Heroku-compatible settings
    app.run(debug=False, host='0.0.0.0', port=port)