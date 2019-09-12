from application import app
from application import admin_views
from application.chat_app import socketio




if __name__ == '__main__':
    socketio.run(app)
