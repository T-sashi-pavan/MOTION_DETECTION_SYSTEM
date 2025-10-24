#!/bin/bash

# Heroku Deployment Script for Motion Detection System
echo "🚀 Deploying Motion Detection System to Heroku..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "🔐 Please login to Heroku first:"
    heroku login
fi

# Get app name from user
read -p "Enter your Heroku app name (e.g., my-motion-detector): " APP_NAME

if [ -z "$APP_NAME" ]; then
    echo "❌ App name cannot be empty"
    exit 1
fi

echo "📝 Creating Heroku app: $APP_NAME"

# Create Heroku app
if heroku create $APP_NAME; then
    echo "✅ Heroku app created successfully"
else
    echo "⚠️  App might already exist, continuing with deployment..."
fi

# Initialize Git if not already done
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Motion Detection System"
fi

# Add Heroku remote
echo "🔗 Connecting to Heroku..."
heroku git:remote -a $APP_NAME

# Deploy to Heroku
echo "🚀 Deploying to Heroku..."
git add .
git commit -m "Deploy motion detection system" || echo "No changes to commit"
git push heroku main

# Open the app
echo "🌐 Opening your deployed app..."
heroku open -a $APP_NAME

echo ""
echo "🎉 Deployment Complete!"
echo "==============================================="
echo "📱 Your Motion Detection System is now live at:"
echo "   https://$APP_NAME.herokuapp.com"
echo ""
echo "✨ Key Features:"
echo "   📷 Each device uses its own camera"
echo "   🔒 Privacy-focused (data stays on device)"
echo "   📱 Works on mobile, tablet, desktop"
echo "   🌐 Accessible from anywhere in the world"
echo ""
echo "📝 Next Steps:"
echo "   1. Share the URL with others"
echo "   2. Test on different devices"
echo "   3. Monitor usage with: heroku logs --tail -a $APP_NAME"
echo "==============================================="