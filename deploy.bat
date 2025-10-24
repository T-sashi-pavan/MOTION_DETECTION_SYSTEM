@echo off
echo 🚀 Deploying Motion Detection System to Heroku...

REM Check if Heroku CLI is installed
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Heroku CLI not found. Please install it first:
    echo    https://devcenter.heroku.com/articles/heroku-cli
    pause
    exit /b 1
)

REM Check if user is logged in to Heroku
heroku auth:whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo 🔐 Please login to Heroku first:
    heroku login
)

REM Get app name from user
set /p APP_NAME=Enter your Heroku app name (e.g., my-motion-detector): 

if "%APP_NAME%"=="" (
    echo ❌ App name cannot be empty
    pause
    exit /b 1
)

echo 📝 Creating Heroku app: %APP_NAME%

REM Create Heroku app
heroku create %APP_NAME%
if %errorlevel% neq 0 (
    echo ⚠️  App might already exist, continuing with deployment...
)

REM Initialize Git if not already done
if not exist ".git" (
    echo 🔧 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit - Motion Detection System"
)

REM Add Heroku remote
echo 🔗 Connecting to Heroku...
heroku git:remote -a %APP_NAME%

REM Deploy to Heroku
echo 🚀 Deploying to Heroku...
git add .
git commit -m "Deploy motion detection system"
git push heroku main

REM Open the app
echo 🌐 Opening your deployed app...
heroku open -a %APP_NAME%

echo.
echo 🎉 Deployment Complete!
echo ===============================================
echo 📱 Your Motion Detection System is now live at:
echo    https://%APP_NAME%.herokuapp.com
echo.
echo ✨ Key Features:
echo    📷 Each device uses its own camera
echo    🔒 Privacy-focused (data stays on device)
echo    📱 Works on mobile, tablet, desktop
echo    🌐 Accessible from anywhere in the world
echo.
echo 📝 Next Steps:
echo    1. Share the URL with others
echo    2. Test on different devices
echo    3. Monitor usage with: heroku logs --tail -a %APP_NAME%
echo ===============================================
pause