import requests
import json
from . import config

def like_message(message_id):
    url = "http://47.94.147.186:8503/like_message"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "x-access-token": config.token,
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data = {"message_id": message_id}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    except Exception as e:
        return str(e)