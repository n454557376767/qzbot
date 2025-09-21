import requests
import json
from . import config



def get_messages(category_id, page, per_page):
    
    url = f"http://47.94.147.186:8503/v3/get_message?category_id={category_id}&page={page}&per_page={per_page}"
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
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
       return None, f"请求出错: {str(e)}"
