# Motion Detection System

🎥 **Live Demo:** [https://motion-detection-system-e7vf.onrender.com/](https://motion-detection-system-e7vf.onrender.com/)

An advanced motion detection system that uses computer vision and machine learning to detect and track human movement in real-time.

## ✨ Key Features

- **🎯 Real-Time Motion Detection** - Instant detection of human movement
- **👥 Multi-Person Tracking** - Detect and count multiple people simultaneously
- **🤖 AI-Powered Detection** - Uses MediaPipe for accurate human pose detection
- **📱 Cross-Platform** - Works on desktop, mobile, and tablets
- **🔒 Privacy First** - All processing happens on your device
- **📊 Live Statistics** - Real-time people counting and motion analysis
- **🌐 Web-Based** - No installation required, just open in browser

## 🚀 Quick Start

1. **Visit the Live Demo** 
   - Open [https://motion-detection-system-e7vf.onrender.com/](https://motion-detection-system-e7vf.onrender.com/) in your browser

2. **Allow Camera Access**
   - Click "Allow" when prompted for camera permissions
   - Ensure you're using HTTPS (required for camera access)

3. **Start Detection**
   - Move in front of your camera to see real-time motion detection
   - The system will automatically detect and count people
   - Green boxes will appear around detected humans

## 🔧 Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript (WebRTC)
- **Backend:** Python Flask
- **Computer Vision:** OpenCV, MediaPipe
- **Machine Learning:** NumPy for data processing
- **Deployment:** Render (Cloud Platform)

## 📁 Project Structure

```
motion-detection-system/
├── 📄 app.py                    # Main Flask application
├── 📄 motion_detection_CV.py    # Advanced motion detection with ML
├── 📄 web_motion_detector.py    # Web-based motion detection
├── 📄 heroku_app.py             # Web application entry point
├── 📁 templates/
│   ├── 📄 index.html            # Main web interface
│   └── 📄 index_enhanced.html   # Enhanced UI version
├── 📄 requirements.txt          # Python dependencies
├── 📄 Procfile                  # Process configuration
└── 📄 README.md                 # This documentation
```

## 🎯 How It Works

The system uses multiple detection methods for maximum accuracy:

1. **Face Detection** 🔍
   - Uses MediaPipe to detect faces and estimate full body positions
   - Excellent for detecting multiple people

2. **Pose Estimation** 🤸‍♂️
   - Analyzes body landmarks and posture
   - Great for single person tracking

3. **Motion Analysis** 🏃‍♂️
   - Background subtraction to detect movement
   - Filters out non-human motion using shape analysis

4. **Smart Filtering** 🧠
   - Combines all methods and removes duplicate detections
   - Uses skin color detection for human verification

## 🌐 Browser Compatibility

| Browser | Desktop | Mobile | Status |
|---------|---------|---------|---------|
| Chrome | ✅ | ✅ | Recommended |
| Firefox | ✅ | ✅ | Fully Supported |
| Safari | ✅ | ✅ | Fully Supported |
| Edge | ✅ | ✅ | Fully Supported |

## 🔒 Privacy & Security

- ✅ **No Data Collection** - Camera data never leaves your device
- ✅ **Local Processing** - All analysis happens in your browser
- ✅ **HTTPS Secure** - Encrypted connection for camera access
- ✅ **No Storage** - No videos or images are saved anywhere

## ⚡ Performance Tips

- **Good Lighting** 💡 - Works best in well-lit environments
- **Stable Connection** 🌐 - Ensure good internet for smooth experience
- **Modern Browser** 🔄 - Use latest browser versions for best performance
- **Camera Quality** 📹 - Higher resolution cameras provide better detection

## 🛠️ Local Development

Want to run this locally? Here's how:

```bash
# Clone the repository
git clone <repository-url>
cd motion-detection-system

# Install dependencies
pip install -r requirements.txt

# Run the application
python heroku_app.py

# Open in browser
# Navigate to http://localhost:5000
```

## 🆘 Troubleshooting

**Camera Not Working?**
- Ensure you're using HTTPS (camera access requirement)
- Check browser permissions for camera access
- Try refreshing the page and allowing permissions again

**Poor Detection?**
- Improve lighting conditions
- Move closer to the camera
- Ensure there's contrast between you and the background

**Slow Performance?**
- Close other browser tabs
- Check your internet connection
- Try using Chrome for best performance

## 📞 Support

Having issues? Here's how to get help:
- 📧 Create an issue in the repository
- 📖 Check the troubleshooting section above
- 🔍 Ensure your browser supports WebRTC

---

**Made with using Python, OpenCV, and MediaPipe**