import requests
import json
from . import config

def sign_in():
    
    url = "http://47.94.147.186:8503/online_qingzhougood"
    
    
    headers = {
        "Accept-Language": "zh-cn,zh;q=0.5",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "x-access-token": config.token,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15; ALI-AN00 Build/HONORALI-AN00)",
        "Host": "47.94.147.186:8503",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    try:
        response = requests.post(url, headers=headers, data="")
        
        return response.status_code, response.json()
    except Exception as e:
        
        return f"请求出错：{str(e)}"
