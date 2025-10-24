# Simple wrapper to fix Render deployment
from heroku_app import app

if __name__ == '__main__':
    app.run()