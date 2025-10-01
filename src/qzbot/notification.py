import requests
from . import config

class Notification:
    def __init__(self):
        self.base_url = "http://47.94.147.186:8503"
        self.headers = {
            'Host': "47.94.147.186:8503",
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Accept-Language': "zh-cn,zh;q=0.5",
            'Accept-Charset': "UTF-8",
            'x-access-token': config.token
        }

    def get_notification(self, page):
        if not config.token:
            return "请先在config模块中设置token"
            
        url = f"{self.base_url}/notification_list?page={page}"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
