import socketio

sio = socketio.Client()

@sio.on("new_message")
def on_new_message(data):
    print("CLIENT 1:", data)

@sio.event
def connect():
    print("Client 1 bağlandı")
    sio.emit("chat_message", "Hello from Client 1")

sio.connect("http://localhost:3000")
sio.wait()
