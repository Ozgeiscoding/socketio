import socketio
import eventlet

sio = socketio.Server()  

@sio.event
def connect(sid, environ):
    print("Client connected")
    sio.emit('welcome', "Welcome to the Socket.IO server!", to=sid)

@sio.event
def disconnect(sid):
    print("Client disconnected")

if __name__ == "__main__":
    print("Server running on port 5000...")
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
