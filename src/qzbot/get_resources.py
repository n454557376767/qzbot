import requests
import json
from . import config


def get_resources(category_id):
    url = "http://47.94.147.186:8503/get_resources"
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    params = {
        "category_id": category_id
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        return response.status_code, response.json()
    except Exception as e:
        return None, f"请求出错: {str(e)}"
     