from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from chatbot_mydata.model_load import MyModel

app = Flask(__name__)
app.config["SECRET_KEY"] = "ffff111jjj52"
socketio = SocketIO(app, cors_allowed_origins="*")
mm = MyModel()


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):

    send({'type': 'user_message', 'content': msg}, broadcast=True)
    print("Received message: " + msg)
    # 응답 생성 로직 호출
    response = generate_response(msg)
    send({'type': 'server_message', 'content': response}, broadcast=True)

#응답 생성 로직
def generate_response(msg):
    output = mm.predict(msg)
    return output

if __name__ == "__main__":
    socketio.run(app, host="192.168.141.21", port=5000)
