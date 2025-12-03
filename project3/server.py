import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print("Bir kullanıcı bağlandı:", sid)

@sio.on("chat_message")
def handle_chat_message(sid, data):
    print(f"Mesaj alındı: {data}")
    # Mesajı olduğu gibi tüm istemcilere gönder
    sio.emit("new_message", data)

@sio.event
def disconnect(sid):
    print("Bir kullanıcı ayrıldı:", sid)

if __name__ == "__main__":
    print("Sunucu çalışıyor: http://localhost:3000")
    eventlet.wsgi.server(eventlet.listen(("", 3000)), app)
