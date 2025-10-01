import requests
import json
from . import config

class Post:
    def __init__(self):
        self.base_url = "http://47.94.147.186:8503"
        self.headers = {
            "Accept-Language": "zh-cn,zh;q=0.5",
            "Accept-Charset": "UTF-8",
            "x-access-token": config.token,
            "Content-Type": "application/json",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
            "Host": "47.94.147.186:8503",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }

    def send_post(self, title, content, category_id, message_type=None, is_markdown=None):
        if not config.token:
            return "请先在config模块中设置token"
        
        url = f"{self.base_url}/post_message"
        data = {
            "category_id": category_id,
            "content": content
        }
        
        if is_markdown:
            data["is_markdown"] = is_markdown
        if message_type:
            data["message_type"] = message_type
            
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def like_message(self, message_id):
        if not config.token:
            return "请先在config模块中设置token"
            
        url = f"{self.base_url}/like_message"
        data = {"message_id": message_id}
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return str(e)

    def get_messages(self, category_id, page, per_page):
        url = f"{self.base_url}/v3/get_message?category_id={category_id}&page={page}&per_page={per_page}"
        
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except requests.RequestException as e:
            return f"请求出错: {str(e)}"
            
    def reply_to_message(self, content, category_id, referenced_message_id):
        if not config.token:
            return "请先在config模块中设置token"
            
        url = f"{self.base_url}/post_referenced_message"
        data = {
            "content": content,
            "category_id": category_id,
            "referenced_message_id": referenced_message_id
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
    