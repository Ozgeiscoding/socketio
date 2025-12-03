import socketio

# Connect to server
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")
    # Send login event with JSON data
    sio.emit("login", {"username": "Ali", "level": 5})

@sio.event
def login_response(data):
    # Print the custom response from server
    print(data)

@sio.event
def disconnect():
    print("Disconnected from server")

sio.connect("http://localhost:5000")
sio.wait()
