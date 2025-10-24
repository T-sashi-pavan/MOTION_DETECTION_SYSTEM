"""
Deployment Helper for Motion Detection System
This script helps set up public access for the motion detection system
"""

import socket
import subprocess
import platform
import sys
import os

def get_local_ip():
    """Get the local IP address"""
    try:
        # Connect to a remote server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "localhost"

def check_python_packages():
    """Check if required packages are installed"""
    required_packages = ["flask", "opencv-python", "mediapipe", "numpy"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            if package == "opencv-python":
                try:
                    __import__("cv2")
                except ImportError:
                    missing_packages.append(package)
            else:
                missing_packages.append(package)
    
    return missing_packages

def install_packages(packages):
    """Install missing packages"""
    if not packages:
        return True
    
    print("Installing missing packages...")
    for package in packages:
        print(f"Installing {package}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", package], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Failed to install {package}: {result.stderr}")
            return False
        else:
            print(f"✅ {package} installed successfully")
    
    return True

def generate_public_access_info(local_ip, port=5000):
    """Generate public access information"""
    print("\n" + "="*70)
    print("🎯 MOTION DETECTION SYSTEM - PUBLIC ACCESS SETUP")
    print("="*70)
    print("\n📱 LOCAL ACCESS:")
    print(f"   http://localhost:{port}")
    print(f"   http://127.0.0.1:{port}")
    
    print("\n🌐 NETWORK ACCESS (Same WiFi/LAN):")
    print(f"   http://{local_ip}:{port}")
    
    print("\n📱 MOBILE/TABLET ACCESS:")
    print(f"   Open browser and go to: http://{local_ip}:{port}")
    
    print("\n🔧 FIREWALL SETUP:")
    if platform.system() == "Windows":
        print("   Windows: Allow Python through Windows Firewall")
        print("   Settings > Update & Security > Windows Security > Firewall")
    else:
        print(f"   Allow port {port} through your firewall")
    
    print("\n🌍 INTERNET ACCESS (Advanced):")
    print("   Option 1: Use ngrok (recommended for testing)")
    print("   Option 2: Port forwarding on your router")
    print("   Option 3: Deploy to cloud (Heroku, AWS, etc.)")
    
    print("\n🔥 NGROK SETUP (Easy Public Access):")
    print("   1. Download ngrok: https://ngrok.com/download")
    print("   2. Sign up for free account")
    print("   3. Install ngrok")
    print(f"   4. Run: ngrok http {port}")
    print("   5. Share the public URL provided by ngrok")
    
    print("\n" + "="*70)

def main():
    """Main deployment setup function"""
    print("🚀 Setting up Motion Detection System for Public Access...")
    
    # Check Python packages
    missing = check_python_packages()
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        install_choice = input("Install missing packages? (y/n): ").lower()
        if install_choice == 'y':
            if not install_packages(missing):
                print("❌ Failed to install some packages. Please install manually.")
                return False
        else:
            print("❌ Please install missing packages manually and try again.")
            return False
    else:
        print("✅ All required packages are installed!")
    
    # Get network information
    local_ip = get_local_ip()
    
    # Generate access information
    generate_public_access_info(local_ip)
    
    return True

if __name__ == "__main__":
    if main():
        print("\n🎯 Setup complete! Ready to deploy Motion Detection System")
        print("📝 Next steps:")
        print("   1. Run: python web_motion_detector.py")
        print("   2. Share the network URL with others")
        print("   3. For internet access, use ngrok or cloud deployment")
    else:
        print("\n❌ Setup failed. Please resolve issues and try again.")