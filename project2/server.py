import socketio

# Create a Socket.IO server
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Handle "login" event
@sio.event
def login(sid, data):
    username = data.get("username", "Guest")
    level = data.get("level", 0)
    message = f"Hello {username}! Your level is {level}."
    # Emit response back to the client
    sio.emit("login_response", message, to=sid)

if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    print("Server running on http://localhost:5000")
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)

