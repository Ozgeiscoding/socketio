import socketio

sio = socketio.Client()

@sio.on("new_message")
def on_new_message(data):
    print("CLIENT 2 RECEIVED:", data)

@sio.event
def connect():
    print("Client 2 connected to server")
    # Bu istemci de bir mesaj gönderiyor
    sio.emit("chat_message", "Hello from Client 2")

@sio.event
def disconnect():
    print("Client 2 disconnected")

sio.connect("http://localhost:3000")
sio.wait()
