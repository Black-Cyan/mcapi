# Minecraft Server Status API

## 简介 / Introduction
这是一个基于 Flask 框架开发的 API 服务，用于查询 Minecraft 服务器的状态信息。它允许用户通过提供服务器的 IP 地址和端口号来获取服务器的在线状态、玩家数量、版本信息等。

## 准备工作 / Preparation
- Python 3.11 以上
- 安装所需的 Python 包，可通过以下命令安装：
```bash
pip install flask flask-cors mcstatus
```

## 使用方法
### 克隆本仓库
```git
git clone https://github.com/Black-Cyan/mcapi
```

### 运行代码
运行 `main.py` 文件来启动 Flask 应用：
```bash
python main.py
```
应用将在 `http://0.0.0.0:5000` 上启动。由于启用了跨域，配置了反向代理后使用其他端口也能访问后端代码。

### 查询服务器状态
发送 GET 请求到 `/api/${edition}/status` 端点，并提供服务器的 IP 地址和端口号（可选，Bedrock Edition 默认为 19132，Java Edition 默认为 25565）作为查询参数。例如：
```
GET http://localhost/api/bedrock/status?ip=mc.example.com&port=19132
```

#### 响应示例
如果服务器在线，响应将包含服务器的详细信息：
```json
{
    "online": true,
    "ip": "x.x.x.x",
    "port": 19132,
    "players_online": 5,
    "players_max": 20,
    "version": "1.19.80",
    "motd": "Welcome to our server!"
}
```
如果服务器离线或出现错误，响应将包含错误信息：
```json
{
    "online": false,
    "error": "Timed out."
}
```
