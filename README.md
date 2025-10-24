# Motion Detection System - Heroku Deployment

A client-side motion detection system where each device uses its own camera.

## Features
- 📱 Client-side camera access (each device uses its own camera)
- 🎯 Real-time motion detection
- 👥 People counting estimation
- 🔒 Privacy-focused (data stays on device)
- 📊 Live statistics
- 🌐 Cross-platform compatibility

## Heroku Deployment Instructions

### Prerequisites
1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Create a free Heroku account: https://signup.heroku.com/

### Deploy to Heroku
1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**
   ```bash
   heroku create your-motion-detection-app
   ```

3. **Initialize Git repository (if not already done)**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Connect to Heroku**
   ```bash
   heroku git:remote -a your-motion-detection-app
   ```

5. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

6. **Open your app**
   ```bash
   heroku open
   ```

### Your Public URL
After deployment, your app will be available at:
`https://your-motion-detection-app.herokuapp.com`

## How It Works
- Each device that visits the URL uses its own camera
- Motion detection runs entirely in the browser using JavaScript
- No server-side camera processing (lightweight deployment)
- Works on mobile phones, tablets, and desktop computers

## File Structure
```
├── heroku_app.py          # Main Flask application
├── templates/
│   └── index.html         # Client-side motion detection interface
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku process configuration
├── runtime.txt           # Python version specification
└── README.md             # This file
```

## Privacy & Security
- ✅ Camera data never leaves the user's device
- ✅ No video is uploaded to servers
- ✅ All processing happens client-side
- ✅ HTTPS enabled by default on Heroku

## Browser Compatibility
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting
- Ensure HTTPS is enabled (required for camera access)
- Allow camera permissions when prompted
- Works best with good lighting conditions
- Requires modern browser with WebRTC support