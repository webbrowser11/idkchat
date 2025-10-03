#idk
from flask import Flask, request, send_file
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
message_file = "message.txt"
@app.route("/", methods=["GET"])
@app.route("/embed.html", methods=["GET"])
def serve_embed():
    return send_file("embed.html", mimetype="text/html")
@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "GET":
        try:
            with open(message_file, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "No messages found", 404
    else:
        msg = request.data.decode("utf-8").strip()
        with open(message_file, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
        return "Message sent"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)