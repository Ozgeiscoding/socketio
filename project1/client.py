import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server!")

@sio.event
def welcome(data):
    print("Server says:", data)

@sio.event
def disconnect():
    print("Disconnected from server!")

if __name__ == "__main__":
    sio.connect('http://localhost:5000')
    sio.wait()
