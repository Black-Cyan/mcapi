from flask import Flask, jsonify, request
from flask_cors import CORS
from mcstatus import BedrockServer, JavaServer

app = Flask(__name__)
CORS(app)


def clean_motd(motd):
    if isinstance(motd, str):
        return motd
    elif isinstance(motd, list):
        return " ".join([clean_motd(item) for item in motd])
    elif hasattr(motd, "text"):
        return motd.text
    return str(motd)


def try_get_data(flag, ip, port):
    try:
        server = BedrockServer.lookup(f"{ip}:{port}") if flag == 0 else JavaServer.lookup(f"{ip}:{port}")
        status = server.status()

        clean_motd_text = clean_motd(status.motd)

        return jsonify({
            "online": True,
            "ip": ip,
            "port": port,
            "players_online": status.players.online,
            "players_max": status.players.max,
            "version": status.version.name,
            "motd": clean_motd_text,
        })
    except Exception as e:
        return jsonify({
            "online": False,
            "error": str(e)
        })


@app.route("/api/bedrock/status", methods=["GET"])
def bedrock_status():
    ip = request.args.get("ip")
    port = int(request.args.get("port", 19132))
    return try_get_data(0, ip, port)


@app.route("/api/java/status", methods=["GET"])
def java_status():
    ip = request.args.get("ip")
    port = int(request.args.get("port", 25565))
    return try_get_data(1, ip, port)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)