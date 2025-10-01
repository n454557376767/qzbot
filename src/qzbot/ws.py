from socketio import Client
import time
from . import config

class Ws:
    def __init__(self):
        self.base_url = "http://47.94.147.186:8503"
        self.sio = None
        self.is_connected = False
        self.callbacks = {
            'connect': None,
            'disconnect': None,
            'new_message': None,
            'status': None,
            'join_response': None,
            'join_error': None
        }

    def connect(self, transports=None):
        if not config.token:
            return "请先在config模块中设置token"
            
        if self.is_connected:
            return "已经连接"

        try:
            # 创建客户端实例
            self.sio = Client(reconnection=False)
            
            # 注册事件处理函数
            @self.sio.event
            def connect():
                self.is_connected = True
                if self.callbacks['connect']:
                    self.callbacks['connect']()

            @self.sio.on('connect_error')
            def on_connect_error(data):
                if self.callbacks['connect']:
                    self.callbacks['connect'](f"连接错误: {data}")

            @self.sio.on('disconnect')
            def on_disconnect():
                self.is_connected = False
                if self.callbacks['disconnect']:
                    self.callbacks['disconnect']()

            @self.sio.on('status')
            def on_status(data):
                if self.callbacks['status']:
                    self.callbacks['status'](data)

            @self.sio.on('new_message')
            def on_new_message(data):
                if self.callbacks['new_message']:
                    self.callbacks['new_message'](data)

            @self.sio.on('join_response')
            def on_join_response(data):
                if self.callbacks['join_response']:
                    self.callbacks['join_response'](data)

            @self.sio.on('join_error')
            def on_join_error(data):
                if self.callbacks['join_error']:
                    self.callbacks['join_error'](data)

            # 连接到服务器
            transport_list = transports or ['polling', 'websocket']
            self.sio.connect(
                self.base_url,
                headers={'x-access-token': config.token},
                transports=transport_list,
                wait_timeout=30
            )
            return "连接成功"
        except Exception as e:
            return f"连接失败: {str(e)}"

    def disconnect(self):
        if self.sio and self.is_connected:
            self.sio.disconnect()
            self.is_connected = False
            return "已断开连接"
        return "未连接"

    def join_category(self, category_id):
        if not self.is_connected:
            return "尚未连接"
        
        try:
            self.sio.emit('join_category', {'category_id': category_id})
            return "已发送加入请求"
        except Exception as e:
            return f"发送失败: {str(e)}"

    def set_callback(self, event, callback):
        
        if event in self.callbacks:
            self.callbacks[event] = callback
            return True
        return False

    def wait(self, seconds):
        
        if self.is_connected:
            time.sleep(seconds)
            return f"等待了 {seconds} 秒"
        return "未连接"
