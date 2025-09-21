import requests
import json
from . import config

def send_post(title, content, category_id, message_type, is_markdown):
    if not config.token:
        return None, "请先调用set_token函数设置token"
    
    url = "http://47.94.147.186:8503/post_message"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "x-access-token": config.token,
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 91; K-91 Build/NoneK91)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    
    data = {
        "category_id": category_id,
        "content": content
    }
    
    
    if is_markdown:
        data["is_markdown"] = is_markdown
    if message_type:
        data["message_type"] = message_type
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return (response.status_code, response.json())
    except Exception as e:
        return None, f"请求出错: {str(e)}"
        
        