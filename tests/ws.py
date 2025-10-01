import qzbot

# 设置Token
qzbot.set_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAzLCJ1c2VybmFtZSI6Im5tMTIzQG91dGxvb2suY29tIiwiZGV2aWNlX2lkIjoiZjRlMzRjYjBhMjBhM2RiYiJ9.ZDET4wW-fHwJj-WjuuzMdn2oyAE8eaGnKddEc-CX_Xw")

# 创建Ws实例
ws = qzbot.Ws()

# 定义回调函数
def on_connect():
    print("✅ 连接成功，正在加入分区 1...")
    ws.join_category(1)

def on_new_message(data):
    print(f"\n💬 收到新消息:")
    print(f"   用户: {data.get('username')}")
    print(f"   内容: {data.get('content')}")
    print(f"   时间: {data.get('timestamp')}")

def on_join_response(data):
    print(f"✅ 加入分区成功: {data}")

def on_disconnect():
    print("🔌 已断开连接")

# 设置回调
ws.set_callback('connect', on_connect)
ws.set_callback('new_message', on_new_message)
ws.set_callback('join_response', on_join_response)
ws.set_callback('disconnect', on_disconnect)

# 连接并开始监听
result = ws.connect(transports=['polling'])  # 可以指定传输方式
print(result)

if "成功" in result:
    print("⏳ 正在监听消息（30秒）...")
    ws.wait(30)  # 保持连接30秒
    ws.disconnect()
