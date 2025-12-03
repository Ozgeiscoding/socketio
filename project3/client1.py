import socketio

sio = socketio.Client()

@sio.on("new_message")
def on_new_message(data):
    print("CLIENT 1 RECEIVED:", data)

@sio.event
def connect():
    print("Client 1 connected to server")
    # Bu istemci sunucuya mesaj gönderiyor
    sio.emit("chat_message", "Hello from Client 1")

@sio.event
def disconnect():
    print("Client 1 disconnected")

sio.connect("http://localhost:3000")
sio.wait()
