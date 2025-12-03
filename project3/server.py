import socketio
import eventlet

# Sunucu oluştur
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Bir istemci bağlandığında
@sio.event
def connect(sid, environ):
    print("Bir kullanıcı bağlandı:", sid)

# chat_message olayı alındığında
@sio.on("chat_message")
def chat_message(sid, data):
    print("Mesaj alındı:", data)
    # Tüm istemcilere mesaj yayını
    sio.emit("new_message", f"Ali says: {data}")

# Bir istemci ayrıldığında
@sio.event
def disconnect(sid):
    print("Bir kullanıcı ayrıldı:", sid)

if __name__ == "__main__":
    print("Sunucu çalışıyor: http://localhost:3000")
    eventlet.wsgi.server(eventlet.listen(("", 3000)), app)
