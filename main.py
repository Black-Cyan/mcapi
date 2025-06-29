# Copyright (c) 2025 Black Cyan.

from flask import Flask, jsonify, request
from flask_cors import CORS
from mcstatus import BedrockServer, JavaServer

app = Flask(__name__)
# 跨域
CORS(app)

def try_get_data(flag, ip, port):
    try:
        server = BedrockServer.lookup(f"{ip}:{port}") if flag == 0 else JavaServer.lookup(f"{ip}:{port}")
        status = server.status()
        return jsonify({
            "online": True,
            "ip": ip,
            "port": port,
            # 在线玩家数
            "players_online": status.players.online,
            # 服务器最大玩家数
            "players_max": status.players.max,
            # 服务端版本
            "version": status.version.name,
            "motd": status.motd,
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